from odoo import models, fields, api

class Alumnos(models.Model):
   _name = 'prueba.alumnos'
   _description = 'Tabla para el control de alumnos'
   _rec_name = 'nombre'

   nombre = fields.Char("Nombre del alumno", required=True)
   apellido_paterno = fields.Char("Apellido Paterno", required=True)
   apellido_materno = fields.Char("Apellido Materno", required=True)
   genero = fields.Selection([('masculino','Masculino'),('femenico','Femenino')],
				 required = True)
   edad = fields.Integer("Edad")
   materia_ids = fields.Many2many('prueba.materia',
				  'materia_alumno_rel',
				  'materia_id',
				  'alumno_id',
				  string="Materias")
