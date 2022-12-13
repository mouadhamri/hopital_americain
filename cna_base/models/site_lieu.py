# -*- coding: utf-8 -*-

from odoo import api, fields, models

class SiteLieu(models.Model):
    _name = 'site.lieu'

    name = fields.Char(required=True, string='Nom')
    site_id = fields.Many2one('site.site', 'Site', required=True)
