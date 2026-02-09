# 💨 Proyecto Final: Base de Datos - Psicodelia Smoke Shop

[cite_start]Este repositorio contiene el desarrollo integral de una solución de gestión de datos para **Psicodelia Smoke Shop**, una empresa establecida en Tijuana, B.C., enfocada en la comercialización de productos de vapeo y accesorios[cite: 21, 25]. El proyecto abarca desde el diseño relacional robusto hasta la migración automatizada a entornos NoSQL.

## 👥 Integrantes
* [cite_start]**Ramirez Cardenas Luis Armando** (Matrícula: 2200607) [cite: 14]
* [cite_start]**De La Cruz Ramirez Jeremy Yael** (Matrícula: 1270230) [cite: 12]
* [cite_start]**Esquivel Zarate Enrique** (Matrícula: 1270230) [cite: 13]

[cite_start]**Institución:** Universidad Autónoma de Baja California (UABC) [cite: 1]
[cite_start]**Facultad:** Contaduría y Administración [cite: 2]
[cite_start]**Carrera:** Inteligencia de Negocios [cite: 8]
[cite_start]**Grupo:** 951 [cite: 15]
[cite_start]**Profesor:** Fernando Christian Gandarilla Carrillo [cite: 19]

---

## 🏗️ Arquitectura del Proyecto

El sistema está diseñado para gestionar el ciclo operativo completo de la tienda mediante tres componentes principales:

### 1. Base de Datos Relacional (MySQL)
* [cite_start]**Esquema Principal:** 10 tablas que cubren Clientes, Marcas, Categorías, Productos, Sucursales, Proveedores, Empleados, Compras, Almacén y Facturación [cite: 122-224].
* [cite_start]**Sistema de Auditoría:** 10 tablas espejo que registran automáticamente el tipo de evento (insert, update, delete), el usuario y la fecha para cada operación [cite: 225-299].
* [cite_start]**Automatización:** 30 Triggers para el registro de auditoría [cite: 334-499] [cite_start]y 50 Procedimientos Almacenados que gestionan el CRUD de cada entidad [cite: 500-505].
* [cite_start]**Vistas de Consulta:** Vistas optimizadas para reportes de auditoría y visualización rápida de datos maestros [cite: 1197-1232].

### 2. Migración NoSQL (Python)
* **Automatización:** Script de Python que conecta MySQL con MongoDB de forma dinámica.
* **Transformación:** Conversión de tipos de datos complejos como `Decimal` a `float` y `Date` a `datetime` para compatibilidad con colecciones NoSQL.

---

## 📂 Contenido del Repositorio

| Archivo | Descripción |
| :--- | :--- |
| `Proyecto_Final_BD_Terminado.sql` | Script SQL completo: definición de tablas, procedimientos, triggers y carga de datos. |
| `Proyecto Final_ Base de Datos.pdf` | [cite_start]Documentación técnica con Diagramas Entidad-Relación (DER) y reportes[cite: 27, 108]. |
| `Exportacion de datos _bd.py` | Script para la migración automatizada de datos a MongoDB. |

---

## 🚀 Instrucciones de Configuración

### Requisitos
* **MySQL Server 8.0+**
* **MongoDB Community Server**
* **Python 3.x** (Librerías: `mysql-connector-python`, `pymongo`)

### Instalación
1. [cite_start]**Base de Datos:** Importa el archivo `Proyecto_Final_BD_Terminado.sql` en MySQL Workbench o vía CLI para crear el esquema `Proyecto_Final_Smoke` [cite: 118-121].
2. **Migración:**
   - Asegúrate de tener los servicios de MySQL y MongoDB activos.
   - Ejecuta el script: `python "Exportacion de datos _bd.py"`.

---

## 📊 Conclusión
[cite_start]Este proyecto integra técnicas avanzadas de administración de bases de datos para mejorar la gestión y seguridad de la información[cite: 1567, 1568]. [cite_start]La implementación de procedimientos y triggers permite una trazabilidad total de los movimientos comerciales, facilitando el análisis de datos estratégico[cite: 1569, 1570].

---
*Lideres innovadores construyendo el futuro. [cite_start]#SOFCA* [cite: 17, 18]
