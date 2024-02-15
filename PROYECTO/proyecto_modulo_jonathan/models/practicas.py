from odoo import models, fields

class Practicas(models.Model):
    _name = 'proyecto_modulo_jonathan.practicas'
    _description = 'Prácticas'

    alumnado_id = fields.Many2one('proyecto_modulo_jonathan.alumnado', string='Alumno', required=True)
    empresa_id = fields.Many2one('proyecto_modulo_jonathan.empresa', string='Empresa', required=True)
    fecha_inicio = fields.Date(string='Fecha de Inicio', required=True)
    fecha_fin = fields.Date(string='Fecha de Fin', required=True)
    departamento = fields.Char(string='Departamento en la Empresa')
    actividades = fields.Text(string='Actividades Realizadas')
    tutor_empresa = fields.Char(string='Tutor en la Empresa', required=True)
    horas = fields.Integer(string='Horas de Prácticas')
    evaluacion = fields.Selection([
        ('excelente', 'Excelente'),
        ('bueno', 'Bueno'),
        ('satisfactorio', 'Satisfactorio'),
        ('insuficiente', 'Insuficiente')
        ], string='Evaluación', required=True)
