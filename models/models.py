# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class cotton_candy_bcn(models.Model):
#     _name = 'cotton_candy_bcn.cotton_candy_bcn'
#     _description = 'cotton_candy_bcn.cotton_candy_bcn'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

