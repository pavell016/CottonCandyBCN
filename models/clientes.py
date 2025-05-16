# -*- coding: utf-8 -*-

from odoo import fields, models

class Curso(models.Model):
    _name = 'x_COTTON_CNADY_BCN.clientes'
    _description = "Clinetes del sistema"

    x_id_cliente = fields.Int (string='Identificador', required=True)
    x_name = fields.Char(string='Nombre', required=True)
    x_apellido1 = fields.Char(string='Apellido 1')
    x_apellido2 = fields.Char(string='Apellido 2')
    x_email = fields.Char(string='Email')
    x_telefono = fields.Char(string='Teléfono')
    x_direccion = fields.Text(string='Dirección')
    x_active = fields.Boolean(string='Activo', default=True)

    # Relación con pedidos
    x_id_pedidos = fields.One2many('x_cotton_candy_bcn.pedido', 'id_cliente', string='Pedidos')

    # Restricción SQL para evitar emails duplicados
    _sql_constraints = [
        ('email_unico', 'unique(email)', '¡El email ya está registrado para otro cliente!'),
        ('telefono_unico', 'unique(telefono)', '¡El teléfono ya está registrado para otro cliente!')
    ]