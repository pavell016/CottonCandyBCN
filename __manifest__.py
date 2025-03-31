# -*- coding: utf-8 -*-
{
    'name': "CottonCandyBCN",

    'summary': """Cada pieza de bisuteria esta disenada con pasion y elaborada a mano.
    Fusionamos creatividad y artesania para ofrecerte accesorios que realzan el estilo propio.""",

    'description': "Modulo para gestionar las ventas de CottonCandyBCN.",

    'author': "Lucia Martinez Gutierrez",
    
    'website': "",
    
    'category': 'Sales',
    
    'version': '1.0',
    
    'depends': ['base', 'sale'],

    'data': [
        'security/ir.model.access.csv',
        'views/cliente_views.xml',
        'views/producto_views.xml',
        'views/pedido_views.xml',
        'views/detalle_pedido_views.xml',
        'views/menu_views.xml',
    ],
    
    'installable': True,
    
    'application': True,
}
