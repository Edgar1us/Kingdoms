# -*- coding: utf-8 -*-
# from odoo import http


# class Kingdoms(http.Controller):
#     @http.route('/kingdoms/kingdoms/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kingdoms/kingdoms/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kingdoms.listing', {
#             'root': '/kingdoms/kingdoms',
#             'objects': http.request.env['kingdoms.kingdoms'].search([]),
#         })

#     @http.route('/kingdoms/kingdoms/objects/<model("kingdoms.kingdoms"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kingdoms.object', {
#             'object': obj
#         })
