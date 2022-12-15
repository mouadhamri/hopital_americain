# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ModelImportance(models.Model):
    _name = 'model.importance'
    _description = "Model Importance"

    name = fields.Char(required=True, string='Model')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Critique')], string="Importance")
