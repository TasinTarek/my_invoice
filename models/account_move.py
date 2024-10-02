# -- coding: utf-8 --
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, UserError
from odoo import http
from odoo.http import request
from datetime import datetime
from dateutil import parser

import logging
_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = "account.move"

    decision_number = fields.Char(string="Decision Number") 
    decision_date = fields.Date(string="Decision Date", default=lambda self: fields.Date.today()) 