# -*- coding: utf-8 -*-
# from odoo import http


# class PoxectoSxe(http.Controller):
#     @http.route('/poxecto_sxe/poxecto_sxe/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/poxecto_sxe/poxecto_sxe/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('poxecto_sxe.listing', {
#             'root': '/poxecto_sxe/poxecto_sxe',
#             'objects': http.request.env['poxecto_sxe.poxecto_sxe'].search([]),
#         })

#     @http.route('/poxecto_sxe/poxecto_sxe/objects/<model("poxecto_sxe.poxecto_sxe"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('poxecto_sxe.object', {
#             'object': obj
#         })
