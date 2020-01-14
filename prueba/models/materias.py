from odoo import models, fields, api

class Materias(models.Model):
#   _inherit = 'sale.order'
   _name = 'prueba.materias'
   _description = 'Tabla para el control de Materias'
   _rec_name = 'nombre'

   nombre = fields.Char("Nombre de la Materia ")
   alumos_ids = fields.Many2many('prueba.alumnos',
				'materia_alumno_rel',
				'materia_id',
				'alumno_id',
				string="Alumnos")
