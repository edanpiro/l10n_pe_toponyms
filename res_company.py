# -*- coding: utf-8 -*-


from openerp.osv import osv, fields


class res_company(osv.Model):
    _inherit = 'res.company'

    _columns = {
        'province_id': fields.many2one('res.country.province', 'Provincia'),
        'district_id': fields.many2one('res.country.district', 'District')
    }

    def onchange_district(self, cr, uid, ids, district_id, context=None):
        if district_id:
            state = self.pool.get('res.country.district').browse(cr, uid, district_id)
            return {'value': {'zip': state.code[2:]}}
        return {}
