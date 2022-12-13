# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Site(models.Model):
    _name = 'site.site'

    name = fields.Char(required=True, string='Nom')
    lieu_ids = fields.One2many('site.lieu', 'site_id', 'Lieux')
