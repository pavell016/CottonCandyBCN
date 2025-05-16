# -*- coding: utf-8 -*-

from odoo import fields, models

class LineaPedido(models.Model):
    _name = 'x_lineas_de_detalle_pedidos'
    _description = "Líneas de detalle de pedidos"

    x_pedido_id = fields.Many2one('x_cotton_candy_bcn.pedido', string='Pedido', ondelete='cascade')
    x_producto_id = fields.Many2one('x_cotton_candy_bcn.producto', string='Producto', required=True)
    x_cantidad = fields.Float(string='Cantidad', digits=(12, 2), default=1)
    x_precio_unitario = fields.Float(string='Precio Unitario', digits=(12, 2))
    x_subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)

    @api.depends('x_cantidad', 'x_precio_unitario')
    def _compute_subtotal(self):
        for linea in self:
            linea.x_subtotal = linea.x_cantidad * linea.x_precio_unitario