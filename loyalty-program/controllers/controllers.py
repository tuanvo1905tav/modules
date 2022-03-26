# -*- coding: utf-8 -*-
# from odoo import http


# class Loyalty-program(http.Controller):
#     @http.route('/loyalty-program/loyalty-program', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/loyalty-program/loyalty-program/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('loyalty-program.listing', {
#             'root': '/loyalty-program/loyalty-program',
#             'objects': http.request.env['loyalty-program.loyalty-program'].search([]),
#         })

#     @http.route('/loyalty-program/loyalty-program/objects/<model("loyalty-program.loyalty-program"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('loyalty-program.object', {
#             'object': obj
#         })
