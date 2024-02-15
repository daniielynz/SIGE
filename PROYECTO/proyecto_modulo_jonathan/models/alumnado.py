from odoo import models, fields


class Alumnado(models.Model):
    _name = 'proyecto_modulo_jonathan.alumnado'
    _description = 'Alumnado'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento', required=True)
    direccion = fields.Char(string='Dirección')
    codigo_postal = fields.Char(string='Código Postal')
    email = fields.Char(string='Email')
    ciclo_formativo = fields.Selection([
        ('dam', 'DAM'),
        ('daw', 'DAW'),
        ('asir', 'ASIR')
    ], string='Ciclo Formativo', default='dam', required=True)
    coche = fields.Boolean(string='Tiene Coche')
    otros = fields.Text(string='Otros Datos')
    nota_media = fields.Float(string='Nota Media')
    nota_media_texto = fields.Char(string='Nota Media (Texto)', compute='_calcular_nota_texto', default='Aprobado')

    def _calcular_nota_texto(self):
        for record in self:
            if record.nota_media >= 9:
                record.nota_media_texto = 'Sobresaliente'
            elif record.nota_media >= 7:
                record.nota_media_texto = 'Notable'
            elif record.nota_media >= 5:
                record.nota_media_texto = 'Aprobado'
            else:
                record.nota_media_texto = 'Suspenso'

    empresa_id = fields.Many2one('proyecto_modulo_jonathan.empresa', string='Empresa')
