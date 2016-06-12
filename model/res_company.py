# -*- coding: utf-8 -*-


from openerp import models, fields, api, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    province_id = fields.Many2one('res.country.province', 'Provincia')
    district_id = fields.Many2one('res.country.district', 'District')

    @api.one
    @api.onchange('district_id')
    def onchange_district(self):
        if self.district_id:
            self.zip = self.district_id.code[2:]
        else:
            self.zip = False
