# -*- coding: utf-8 -*-
# from odoo import http


# class OpenAcademy2(http.Controller):
#     @http.route('/open_academy_empty/open_academy_empty', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/open_academy_empty/open_academy_empty/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('open_academy_empty.listing', {
#             'root': '/open_academy_empty/open_academy_empty',
#             'objects': http.request.env['open_academy_empty.open_academy_empty'].search([]),
#         })

#     @http.route('/open_academy_empty/open_academy_empty/objects/<model("open_academy_empty.open_academy_empty"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('open_academy_empty.object', {
#             'object': obj
#         })
