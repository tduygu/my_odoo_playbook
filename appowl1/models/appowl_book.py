# -*- coding: utf-8 -*-
from odoo import models, fields


class AppOwlBook(models.Model):
    _name = 'appowl.book'
    _description = 'AppOwl Book'

    _order = 'date_release desc, name'

    name = fields.Char('Title', required=True)
    short_name = fields.Char('Short Title')
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')

    def name_get(self):
        """ This method used to customize display name of the record """
        result = []
        for record in self:
            rec_name = "%s (%s)" % (record.name, record.date_release)
            result.append((record.id, rec_name))
        return result