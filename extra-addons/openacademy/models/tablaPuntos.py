from odoo import fields, models

class TestModel2(models.Model):
    _name = "test_model2"
    _description = "test_model2"

    nombre = fields.Char(string="Nombre")
    puntos = fields.Integer(string="Puntos")