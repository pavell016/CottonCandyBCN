# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Producto(models.Model):
    _name = 'producto.producto'
    _description = 'Este modelo de datos nos servirá para almacenar la información de los productos de bisutería'

    nombre = fields.Char('Nombre del producto', required=True)
    descripcion = fields.Text('Descripción del producto')
    precio = fields.Float('Precio', required=True)
    stock = fields.Integer('Stock disponible', required=True, default=0)
    categoria = fields.Selection([
        ('collar', 'Collar'),
        ('pulsera', 'Pulsera'),
        ('anillo', 'Anillo'),
        ('pendientes', 'Pendientes'),
    ], string="Categoría", required=True, help="Selecciona la categoría del producto")

    imagen = fields.Binary('Imagen del producto')
    fecha_creacion = fields.Datetime('Fecha de creación', default=fields.Datetime.now)
    es_destacado = fields.Boolean('Destacado', default=False, help="Marca este producto como destacado en la tienda")

    # Primary Key
    # (‘nombre_PK, ‘unique(atributo1, atributo2, atributoN)’, ‘Mensaje de error a mostrar cuando se intenten insertar
    # filas duplicadas’)
    _sql_constraints = [
        ('nombre_unico', 'unique(nombre)', 'El nombre del producto debe ser único.')
    ]
