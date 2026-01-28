"Proyecto final de la materia de Base de Datos Avanzada centrado en el diseño e implementación de una base de datos avanzada para la empresa 'Psicodelia Smoke Shop'. El sistema integra una arquitectura relacional completa en MySQL con 10 tablas principales, procedimientos almacenados para la gestión de datos (CRUD), y un robusto sistema de auditoría automatizado mediante 30 triggers y vistas especializadas. Además, incluye un módulo de migración de datos desarrollado en Python para la exportación de registros hacia una base de datos NoSQL (MongoDB)."

Caracteristicas Tecnicas:
a) Arquitectura de Datos: Diseño de esquemas para la gestión de clientes, productos, inventarios (sucursales), ventas y facturación comercial.

b) Automatización y Auditoría: Implementación de disparadores (triggers) para el registro automático de eventos de inserción, actualización y eliminación en tablas de auditoría dedicadas.

c) Lógica de Negocio: Desarrollo de 50 procedimientos almacenados para centralizar la lógica de lectura y manipulación de datos por ID o de forma masiva.

d) Interoperabilidad (ETL): Script en Python utilizando mysql.connector y pymongo para la conversión de tipos de datos y migración exitosa entre entornos relacionales y no relacionales.

e) Consultas Optimizadas: Creación de vistas personalizadas para reportes rápidos de auditoría y estados actuales de la base de datos.
