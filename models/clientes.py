# -*- coding: utf-8 -*-

from odoo import fields, models

class Curso(models.Model):
    _name = 'COTTON_CNADY_BCN.clientes'
    _description = "Clinetes del sistema"

    id_cliente = fields.Int (string='Identificador', required=True)
    name = fields.Char(string='Nombre', required=True)
    apellido1 = fields.Char(string='Apellido 1')
    apellido2 = fields.Char(string='Apellido 2')
    email = fields.Char(string='Email')
    telefono = fields.Char(string='Teléfono')
    direccion = fields.Text(string='Dirección')
    active = fields.Boolean(string='Activo', default=True)

    # Relación con pedidos
    id_pedidos = fields.One2many('COTTON_CNADY_BCN.pedido', 'id_cliente', string='Pedidos')

    # Restricción SQL para evitar emails duplicados
    _sql_constraints = [
        ('email_unico', 'unique(email)', '¡El email ya está registrado para otro cliente!'),
        ('telefono_unico', 'unique(telefono)', '¡El teléfono ya está registrado para otro cliente!')
    ]