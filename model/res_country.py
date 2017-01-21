# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 Cubic ERP - Teradata SAC (<http://cubicerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from odoo import models, fields, api


class ConventionCountry(models.Model):
    _name = 'convention.country'

    name = fields.Char('Descripcion', required=True)
    code = fields.Char('Codigo', size=2, required=True)


class ResCountry(models.Model):
    _inherit = 'res.country'

    code_sunat = fields.Char('Codigo sunat', help='Tabla 35 sunat')
    convention_id = fields.Many2one('convention.country', 'Convenio tributacion',
                                    help="Tabla 25 SUNAT")


class CountryState(models.Model):
    _inherit = 'res.country.state'

    province_ids = fields.One2many('res.country.province', 'state_id', 'Provinces')


class CountryProvince(models.Model):
    _name = 'res.country.province'
    _description = 'Country State Provinces'

    state_id = fields.Many2one('res.country.state', 'State', required=True)
    name = fields.Char('Province Name', size=64, required=True)
    code = fields.Char('Province Code', size=6, required=True)
    district_ids = fields.One2many('res.country.district', 'province_id', 'Districts')

    _sql_constraints = [
        ('code_uniq','unique(code)','The code of the province must be unique !'),
    ]


class CountryDistrict(models.Model):
    _name = 'res.country.district'
    _description = 'Country State Province Districts'

    province_id = fields.Many2one('res.country.province', 'Province', required=True)
    name = fields.Char('District Name', size=64, required=True)
    code = fields.Char('District Code', size=8, required=True)

    _sql_constraints = [
        ('code_uniq','unique(code)','The code of the district must be unique !')
    ]
