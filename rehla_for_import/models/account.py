from odoo import fields, models,api,_


import base64
import logging

from lxml import etree
from odoo import models, fields, api
from odoo.tools import float_is_zero, float_round


class AccountMove(models.Model):
    _inherit = "account.move"

    invoice_rehla = fields.Char(string="Invoice Number")
    payment_meth = fields.Char(string="Payment Meth")
    booking_id = fields.Char(string="Booking Id")
    trip_initiated = fields.Char(string="Trip Initiated")


