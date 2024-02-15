# -*- coding: utf-8 -*-
# from odoo import http


# class ProyectoModuloJonathan(http.Controller):
#     @http.route('/proyecto_modulo_jonathan/proyecto_modulo_jonathan', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyecto_modulo_jonathan/proyecto_modulo_jonathan/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyecto_modulo_jonathan.listing', {
#             'root': '/proyecto_modulo_jonathan/proyecto_modulo_jonathan',
#             'objects': http.request.env['proyecto_modulo_jonathan.proyecto_modulo_jonathan'].search([]),
#         })

#     @http.route('/proyecto_modulo_jonathan/proyecto_modulo_jonathan/objects/<model("proyecto_modulo_jonathan.proyecto_modulo_jonathan"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyecto_modulo_jonathan.object', {
#             'object': obj
#         })
