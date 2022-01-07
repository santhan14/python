from odoo import fields,models

class schoolprofile(models.model):
    _name="school.profile"

    name =fields.char(string="school Name")
    email=fields.char(string="email")
    phone=fields.char("phone")