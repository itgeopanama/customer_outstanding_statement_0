# -*- coding: utf-8 -*-

from odoo import fields,api,models

class AccountMove(models.Model):
    _inherit="account.move"
    
    new_seq_name = fields.Char(string="New Sequence com")
    new_name = fields.Char(string="New Sequence")
    