# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleLinesExtInh(models.Model):
    _inherit = 'sale.order.line'

    remarks = fields.Char(string='Remarks')
