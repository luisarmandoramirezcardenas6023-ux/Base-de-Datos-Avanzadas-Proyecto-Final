import mysql.connector
from pymongo import MongoClient
from datetime import date, datetime
from decimal import Decimal

# Conexión MySQL
mysql_conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='Proyecto_Final_Smoke'
)

# Conexión MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['proyecto_final_smoke']

# Mapeo: tabla → procedimiento correcto
table_procs = {
    "clients": "get_all_clients",
    "brands": "get_all_brands",
    "category": "get_all_categories",
    "products": "get_all_products",
    "branches": "get_all_branches",
    "suppliers": "get_all_suppliers",
    "employees": "get_all_employees",
    "purchases": "get_all_purchases",
    "store": "get_all_store",
    "commercial_invoice": "get_all_invoices"
}

# Conversión de tipos para MongoDB
def convert_types(record):
    for key, value in record.items():
        if isinstance(value, date) and not isinstance(value, datetime):
            record[key] = datetime.combine(value, datetime.min.time())
        elif isinstance(value, Decimal):
            record[key] = float(value)
    return record

# Exportación por tabla
for table, proc_name in table_procs.items():
    with mysql_conn.cursor(dictionary=True) as cursor:
        cursor.callproc(proc_name)
        for result in cursor.stored_results():
            data = result.fetchall()

        data = [convert_types(doc) for doc in data]

        if data:
            mongo_db[table].insert_many(data)
            print(f"✅ Datos de '{table}' migrados exitosamente.")
        else:
            print(f"⚠️ No hay datos en '{table}'.")

# Cierre de conexiones
mysql_conn.close()
mongo_client.close()
