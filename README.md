# Práctica Odoo | CottonCandyBCN 🍭

## 📝 Descripción del Módulo
Este módulo de gestión comenrcial ha sido desarrollado como parte de una práctica evaluable siguiendo la arquitectura de Odoo, implementa un sistema completo con modelos de datos, vistas y funcionalidades personalizadas.

## 📂 Estructura del Proyecto
```
COTTON_CANDY_BCN/
├── __init__.py
├── __manifest__.py
├── controllers/
├── demo/
├── models/
│   ├── __init__.py
│   ├── clientes.py
│   └── metodosPago.py
│   └── pedidos.py
│   └── productos.py
├── security/
│   └── ir.model.access.csv
├── static/description
│   └── icon.png
├── views/
│   ├── templates.xml
│   ├── clientes_views.xml
│   ├── productos_views.xml
│   └── pedidos_views.xml
│   └── detalle_pedidos_views.xml
│   └── menu_views.xml
└── README.md
```

## 🛠️ Requisitos e Instalación
1. **Requisitos**:
   - Odoo 17 Community Edition
   - Python 3.5+
   - PostgreSQL 9.6+

2. **Instalación**:
   ```bash
   # Copiar la carpeta del módulo a la ruta de addons de Odoo
   cp -r COTTON_CANDY_BCN /ruta/a/odoo/addons/
   
   # Activar el modo desarrollador > Aplicaciones > Actualizar lista
   # Instalar el módulo desde el menú de aplicaciones
   ```

## 📊 Modelos de Datos
1. **Cliente**: Almacena información de los clientes
2. **Producto**: Gestiona el catálogo de productos
3. **Pedido**: Registra los pedidos realizados por clientes
4. **MetodosPago**: Gestiona los diferentes sistemas de pago disponibles para los pedidos

## 📦 Características Principales
✅ Gestión completa de clientes <br>
✅ Catálogo de productos con categorías <br>
✅ Sistema de pedidos con múltiples estados

## 📄 Documentación Adicional
El documento PDF adjunto (PrácticaOdoo.pdf) contiene:
- Explicación detallada del desarrollo
- Capturas de pantalla del proceso
- Pruebas realizadas
- Diagramas de la estructura de datos

## 👩‍💻 Autora
Lucía Martínez Gutiérrez <br>
La Salle Grácia  
