# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Appcms1(http.Controller):
    @http.route('/appcms1/books', type='http', auth="user", website=True)
    def library_books(self):
        return request.render(
            'appcms1.books', {
                'books': request.env['appcms1.book'].search([]),
            })

    @http.route('/appcms1/books/<model("appcms1.book"):book>', type='http', auth="user", website=True)
    def library_book_detail(self, book):
        return request.render(
            'appcms1.book_detail', {
                'book': book,
            })


# from odoo import http


# class Appcms1(http.Controller):
#     @http.route('/appcms1/appcms1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/appcms1/appcms1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('appcms1.listing', {
#             'root': '/appcms1/appcms1',
#             'objects': http.request.env['appcms1.appcms1'].search([]),
#         })

#     @http.route('/appcms1/appcms1/objects/<model("appcms1.appcms1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('appcms1.object', {
#             'object': obj
#         })
