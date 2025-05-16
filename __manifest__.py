# -*- coding: utf-8 -*-
{
    'name': "CottonCandyBCN",

    'summary': """Cada pieza de bisuteria esta disenada con pasion y elaborada a mano.
    Fusionamos creatividad y artesania para ofrecerte accesorios que realzan el estilo propio.""",

    'description': """
        Modulo para gestionar las ventas de CottonCandyBCN.
        
        Características principales:
        - Gestión de clientes
        - Catálogo de productos
        - Gestión de pedidos
        - Seguimiento de ventas
    """,

    'author': "Lucia Martinez Gutierrez",
    
    'website': "https://cottoncandybcn.com",
    
    'category': 'Sales',
    
    'version': '16.0.1.0.0',
    
    'depends': [
        'base',
        'sale',
        'mail',
        'product',
        'contacts'
    ],

    'data': [
        # Security
        'security/ir.model.access.csv',
        'security/cottoncandybcn_security.xml',
        
        # Views
        'views/menu_views.xml',
        'views/cliente_views.xml',
        'views/producto_views.xml',
        'views/pedido_views.xml',
        'views/detalle_pedido_views.xml',
    ],
    
    'images': ['static/description/banner.png'],
    
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
