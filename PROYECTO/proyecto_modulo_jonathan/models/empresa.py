from odoo import models, fields


class Empresa(models.Model):
    _name = 'proyecto_modulo_jonathan.empresa'
    _description = 'Empresa'

    nombre = fields.Char(string='Nombre', required=True)
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    departamento = fields.Selection([
        ('Informatica', 'INFORMATICA'),
        ('Comercio', 'COMERCIO'),
        ('Marketing', 'MARKETING'),
        ('Administracion', 'ADMINISTRACION')
    ], string='Departamento', default='informatica')
    practicas_alumnado_ids = fields.One2many(
        'proyecto_modulo_jonathan.practicas', 'empresa_id', string='Prácticas de Alumnos'
    )
