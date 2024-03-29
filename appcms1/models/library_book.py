# -*- coding: utf-8 -*-
from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'appcms1.book'
    _description = 'Library Book'

    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')
    image = fields.Binary(attachment=True)
    html_description = fields.Html()