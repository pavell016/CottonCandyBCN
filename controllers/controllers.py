# -*- coding: utf-8 -*-
# from odoo import http


# class CottonCandyBcn(http.Controller):
#     @http.route('/cotton_candy_bcn/cotton_candy_bcn', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cotton_candy_bcn/cotton_candy_bcn/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cotton_candy_bcn.listing', {
#             'root': '/cotton_candy_bcn/cotton_candy_bcn',
#             'objects': http.request.env['cotton_candy_bcn.cotton_candy_bcn'].search([]),
#         })

#     @http.route('/cotton_candy_bcn/cotton_candy_bcn/objects/<model("cotton_candy_bcn.cotton_candy_bcn"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cotton_candy_bcn.object', {
#             'object': obj
#         })

