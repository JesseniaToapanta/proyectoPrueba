# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'prueba.course'

    name = fields.Char(string="Title", required=True )
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', string="Responsible", 
			index=True, ondelete='set null')
    session_ids = fields.One2many('prueba.session','course_id')

class Session(models.Model):
    _name = 'prueba.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2),help="Durarion in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner', string='Instructor')
    course_id = fields.Many2one('prueba.course', ondelete='cascade',
				string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Atendees")
