from odoo import models, fields


class tutoriafct(models.Model):
    _name = 'proyecto_modulo_jonathan.tutoriafct'
    _description = 'Tutoría FCT'

    nombre_tutor = fields.Char(string='Nombre del Tutor', required=True)
    departamento = fields.Char(string='Departamento', required=True)
    email_tutor = fields.Char(string='Email')
    telefono_tutor = fields.Char(string='Teléfono')
