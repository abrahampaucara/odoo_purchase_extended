# -*- coding: utf-8 -*-

from odoo import models, fields


class purchase_extended(models.Model):
    _inherit = 'purchase.order'

    nit_number = fields.Char()
    card_add_on = fields.Char()
    business_name = fields.Char()
    authorization_code = fields.Char()
    airplane_ticket = fields.Boolean()
    control_code = fields.Char()

