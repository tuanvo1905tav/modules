# -*- coding: utf-8 -*-
# from odoo import http


# class ProducTest(http.Controller):
#     @http.route('/produc_test/produc_test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/produc_test/produc_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('produc_test.listing', {
#             'root': '/produc_test/produc_test',
#             'objects': http.request.env['produc_test.produc_test'].search([]),
#         })

#     @http.route('/produc_test/produc_test/objects/<model("produc_test.produc_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('produc_test.object', {
#             'object': obj
#         })
