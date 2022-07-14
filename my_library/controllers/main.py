import datetime
import email.utils
from odoo import fields

from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route('/my_library/books', type='http', auth='none')
    def books(self):
        books = request.env['library.book'].sudo().search([])
        html_result = '<html><body><ul>'
        for book in books:
            html_result += "<li> %s </li>" % book.name
        html_result += '</ul></body></html>'
        # return html_result
        return request.make_response(html_result, headers=[
            ('Last-modified', email.utils.formatdate(
                (fields.Datetime.from_string(
                    request.env['library.book'].sudo().search([], order='write_date desc', limit=1).write_date) -
                 datetime.datetime(1970, 1, 1)).total_seconds(), usegmt=True)),
        ])

    @http.route('/my_library/books/json', type='json', auth='none')
    def books_json(self):
        records = request.env['library.book'].sudo().search([])
        return records.read(['name'])

    @http.route('/my_library/all-books/mark-mine', type='http', auth='public')
    def all_books_mark_mine(self):
        books = request.env['library.book'].sudo().search([])
        html_result = '<html><body><ul>'
        for book in books:
            # html_result += f"<li> {request.env.user.partner_id.id} - {book.author_ids.ids} </li>"
            if request.env.user.partner_id.id in book.author_ids.ids:
                html_result += "<li><b> %s </b></li>" % book.name
            else:
                html_result += "<li> %s </li>" % book.name
        html_result += '</ul></body></html>'
        return html_result

    @http.route('/my_library/all-books/mine', type='http', auth='user')
    def all_books_mine(self):
        books = request.env['library.book'].search([('author_ids', 'in', request.env.user.partner_id.ids), ])
        html_result = '<html><body><ul>'
        for book in books:
            html_result += "<li><b>%s</b></li>" % book.name
        html_result += '</ul></body></html>'
        return html_result

    # http: // localhost: 8015 / my_library / book_details?book_id = 2
    @http.route('/my_library/book_details', type='http', auth='none')
    def book_details(self, book_id):
        record = request.env['library.book'].sudo().browse(int(book_id))
        return u'<html><body><h1>%s</h1>Authors: %s' % (
        record.name, u', '.join(record.author_ids.mapped('name')) or 'none')

    # http: // localhost: 8015 / my_library / book_details / 2 - bu calismadi - parametre olarak uid mi bekliyor
    # @http.route("/my_library/book_details/<model('library.book'):book>", type='http', auth='none')
    # def book_details_in_path(self, book):
    #     return self.book_details(book.id)

    # Bu benim hatırladığım ve çalışan /my_library/book_detail/2
    @http.route("/my_library/book_detail/<bid>", type='http', auth='none')
    def book_details_in_path(self, bid):
        return self.book_details(bid)

    @http.route('/my_library/demo_page', type='http', auth='none')
    def book_page(self):
        image_url = '/my_library/static/src/img/odoo.png'
        html_result = """<html>
            <body>
                <img src="%s" />
            </body>
        </html>""" % image_url
        return html_result