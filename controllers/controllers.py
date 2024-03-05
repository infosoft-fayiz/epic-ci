# -*- coding: utf-8 -*-
# from odoo import http


# class Epic-pos-ci(http.Controller):
#     @http.route('/epic-pos-ci/epic-pos-ci', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/epic-pos-ci/epic-pos-ci/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('epic-pos-ci.listing', {
#             'root': '/epic-pos-ci/epic-pos-ci',
#             'objects': http.request.env['epic-pos-ci.epic-pos-ci'].search([]),
#         })

#     @http.route('/epic-pos-ci/epic-pos-ci/objects/<model("epic-pos-ci.epic-pos-ci"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('epic-pos-ci.object', {
#             'object': obj
#         })
