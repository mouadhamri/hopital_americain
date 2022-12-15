# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class Tags(models.Model):
	_name = 'tags.tags'
	_description = "Tags Tags"

	name = fields.Char('Nom', copy=False, default=lambda x: _('New'))
	site_id = fields.Many2one('site.site', 'Site', required=True)
	respo_zone_id = fields.Many2one('res.users', 'Responsable zone')
	last_date_scan = fields.Datetime(string="Dernier date du scan", required=False, compute="compute_last_scan", store=True)
	tag_file = fields.Binary(string="Fichier de tag")
	tag_line_ids = fields.One2many('task.tags.line', 'tag_id', 'Scan')
	is_start_scan = fields.Boolean(string="Tag de démarrage", )
	is_end_scan = fields.Boolean(string="Tag d'arrêt", )
	lieu = fields.Many2one('site.lieu', "Lieu", tracking = True)


	@api.constrains('is_start_scan', 'is_end_scan')
	def _check_start_end_tag(self):
		for tag in self:
			if tag.is_start_scan and tag.is_end_scan:
				raise UserError("Vous pouvez pas avoir un tag de démarrage et d'arrêt en même temps")

	@api.depends('tag_line_ids', 'tag_line_ids.scan_date')
	def compute_last_scan(self):
		for rec in self:
			last_date_scan = False
			if rec.tag_line_ids:
				tag_line_ids = rec.tag_line_ids.filtered(lambda r: r.scan_date)
				if tag_line_ids:
					last_date_scan = tag_line_ids.sorted('scan_date')[-1].scan_date
			rec.last_date_scan = last_date_scan

	@api.model
	def create(self, vals):
		if not vals.get('name') or vals['name'] == _('New'):
			vals['name'] = self.env['ir.sequence'].next_by_code('tags.tags') or ''
		return super(Tags, self).create(vals)

	def action_see_all_scan(self):
		return {
			'name': _('Tout les scan'),
			'type': 'ir.actions.act_window',
			'view_mode': 'tree',
			'res_model': 'task.tags.line',
			'domain': [('tag_id', '=', self.id)],
		}


class Ronde(models.Model):
	_name = 'ronde.ronde'
	_description = "Ronde Ronde"

	name = fields.Char('Ronde', required=True)
	tag_ids = fields.One2many('ronde.tags', 'ronde_id', 'Tags')
	lieu = fields.Many2one('site.lieu', 'Lieu')

	def start_ronde(self):
		if len(self._context.get('active_ids')) > 1:
			raise UserError(_("Vous ne pouvez pas démarrer plusieurs rondes."))

		ctx = {
			'default_project_id': self.env.ref('industry_fsm.fsm_project').id or False,
			'default_partner_id': self.env.user.company_id.partner_id.id or False,
		}
		ronde = self.env['ronde.ronde'].search([('id', '=', self._context.get('active_ids')[0])])
		if ronde:
			ctx['default_name'] = ronde.name
			ctx['default_lieu'] = ronde.lieu and ronde.lieu.id or False
			ctx['default_ronde_id'] = ronde.id

		return {
			'name': _('Ronde'),
			'type': 'ir.actions.act_window',
			'view_mode': 'form',
			'res_model': 'project.task',
			'target': 'current',
			'context': ctx
		}


class RondeTags(models.Model):
	_name = 'ronde.tags'
	_description = "Ronde Tags"

	sequence = fields.Integer(default=1)
	tag_id = fields.Many2one('tags.tags', 'Tag', required=True, ondelete='restrict')
	ronde_id = fields.Many2one('ronde.ronde', 'Ronde')
	is_required = fields.Boolean(string="Obligatoire")
