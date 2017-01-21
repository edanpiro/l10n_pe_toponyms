# -*- coding: utf-8 -*-


from odoo import models, fields, api, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    province_id = fields.Many2one('res.country.province', 'Provincia')
    district_id = fields.Many2one('res.country.district', 'District')

    @api.onchange('district_id')
    def onchange_district(self):
        if self.district_id:
            zip = self.env['res.country.district'].browse(self.district_id.id)
            self.zip = zip.code[2:]
        else:
            self.zip = False
