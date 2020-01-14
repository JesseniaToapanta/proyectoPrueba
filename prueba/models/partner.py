from odoo import models, fields, api
 
class Partner(models.Model):
#   _name = 'prueba.partner '
   _inherit = 'res.partner'

   instructor = fields.Boolean(default=False)
   session_ids = fields.Many2many('prueba.session',string="Attended Sessions", readonly=True)
   other_field = fields.Boolean(default=True)
   other_field2 = fields.Boolean(default=True)
#  res_partner_prueba_session_rel
# prueba_session_res_partner_rel
