# -*- coding: utf-8 -*-

from odoo import fields, models

class MetodoPago(models.Model):
    _name = 'x_cotton_candy_bcn.metodo_pago'
    _description = "Métodos de pago disponibles"

    x_name = fields.Char(string='Nombre', required=True)  # Ej: "Tarjeta", "PayPal", "Efectivo"
    x_descripcion = fields.Text(string='Descripción')
    x_comision = fields.Float(string='Comisión (%)', default=0.0)
    x_active = fields.Boolean(string='Activo', default=True)
    x_es_online = fields.Boolean(string='Pago Online', help="Marca si el pago es digital")

    # Restricción para nombres únicos
    _sql_constraints = [
        ('name_unique', 'unique(x_name)', '¡Este método de pago ya existe!')
    ]