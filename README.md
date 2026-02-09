# 💨 Gestión de Datos y Auditoría: Psicodelia Smoke Shop

Este repositorio contiene el proyecto final para la asignatura de **Base de Datos Avanzadas**. El sistema integra una arquitectura relacional completa en MySQL con un sistema de trazabilidad mediante triggers, además de un motor de migración hacia entornos NoSQL para la escalabilidad de la información.

## 🚬 ¿Qué problemas soluciona?
En la gestión operativa de una tienda de retail (Smoke Shop), el control preciso de inventarios y la seguridad de los registros son críticos. Este software soluciona:
* **Centralización Operativa:** Integra en un solo esquema la gestión de clientes, empleados, sucursales, productos y procesos de facturación.
* **Auditoría Automatizada:** Implementa un sistema de "tablas espejo" que registra cada inserción, edición o eliminación de datos, identificando al usuario y la fecha exacta del cambio.
* **Integridad del Inventario:** Controla existencias mediante niveles de stock mínimo y máximo dentro de la tabla de almacén para evitar desabastos.
* **Escalabilidad NoSQL:** Incluye un puente de integración para migrar datos relacionales a colecciones de MongoDB, permitiendo análisis de datos de gran volumen y flexibilidad.

## 🛠️ Tecnologías Utilizadas
* **Base de Datos Relacional:** MySQL Workbench (Esquema SQL, Triggers y Procedimientos Almacenados).
* **Lenguaje de Integración:** Python 3.x.
* **Conectores:** `mysql-connector-python` y `pymongo`.
* **Base de Datos NoSQL:** MongoDB (para persistencia escalable).
* **Documentación:** Diagramas Entidad-Relación (DER) detallados.

## 📊 Estructura del Sistema
El proyecto se divide en tres capas de datos:
1. **Capa Transaccional:** 10 tablas principales que gestionan el día a día del negocio (Ventas, Clientes, Inventario).
2. **Capa de Auditoría:** 10 tablas y 30 triggers encargados de la trazabilidad y seguridad de la información.
3. **Capa de Abstracción:** Vistas y procedimientos almacenados (CRUD) que facilitan la interacción con el sistema sin manipular el código SQL crudo.

## 📖 Manual de Uso
Para poner en marcha el sistema, siga estas etapas en orden:
1. **Despliegue SQL:** Ejecute el script `Proyecto_Final_BD_Terminado.sql` para crear el esquema `Proyecto_Final_Smoke` y cargar los procedimientos.
2. **Carga de Datos:** Utilice los `CALL` predefinidos en el script para poblar el sistema con información de prueba de sucursales y productos.
3. **Verificación de Auditoría:** Realice cambios en las tablas principales y consulte las `vista_auditoria_` para confirmar el registro de eventos.
4. **Migración:** Ejecute el script de Python para transferir la base de datos de MySQL a MongoDB automáticamente.

## 👥 Desarrolladores
* **Ramirez Cardenas Luis Armando** - (Matrícula: 2200607)
* **De La Cruz Ramirez Jeremy Yael** - (Matrícula: 1270230)
* **Esquivel Zarate Enrique** - (Matrícula: 1270230)

**Institución:** Universidad Autónoma de Baja California (UABC).
**Facultad:** Contaduría y Administración.
**Carrera:** Inteligencia de Negocios.
**Profesor:** Fernando Christian Gandarilla Carrillo.
