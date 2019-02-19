# -*- coding: utf-8 -*-

from odoo import api, fields, models


class EventInherit(models.Model):
    _inherit = "event.event"

    event_cover_poster = fields.Binary(string="Event Image")
