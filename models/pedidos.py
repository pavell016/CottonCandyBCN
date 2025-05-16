# -*- coding: utf-8 -*-

from odoo import fields, models

class Pedido(models.Model):
    _name = 'x_cotton_candy_bcn.pedido'
    _description = "Pedidos de clientes"
    _order = "x_fecha_pedido desc"  # Ordenar por fecha descendente

    # Campos básicos
    x_name = fields.Char(string='Referencia', required=True)
    x_fecha_pedido = fields.Datetime(string='Fecha', default=fields.Datetime.now)
    x_total = fields.Float(string='Total', digits=(12, 2), required=True)
    x_notas = fields.Text(string='Notas')

    # Estados del pedido
    x_estado = fields.Selection(
        selection=[
            ('borrador', 'Borrador'),
            ('confirmado', 'Confirmado'),
            ('en_proceso', 'En proceso'),
            ('enviado', 'Enviado'),
            ('entregado', 'Entregado'),
            ('cancelado', 'Cancelado')
        ],
        string='Estado',
        default='borrador'
    )

    # Relaciones
    x_cliente_id = fields.Many2one(
        'x_COTTON_CNADY_BCN.clientes',  # Nombre técnico del modelo de clientes
        string='Cliente',
        required=True
    )

    x_metodo_pago_id = fields.Many2one(
        'x_cotton_candy_bcn.metodo_pago',
        string='Método de pago',
        required=True
    )

    x_lineas_pedido = fields.One2many(
        'x_cotton_candy_bcn.linea_pedido',  # Modelo de líneas (detalle)
        'x_pedido_id',
        string='Productos'
    )

    # Restricción para total positivo
    _sql_constraints = [
        ('total_positivo', 'CHECK(x_total >= 0)', 'El total debe ser positivo o cero')
    ]