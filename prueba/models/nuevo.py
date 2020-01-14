from odoo import models, fields, api

class FieldsModel(models.Model):
#   _inherit = 'sale.order'
   _name = 'prueba.nuevo'
   
   field_bool = fields.Boolean("Campo tipo Boolean")
   field_int = fields.Integer("Campo tipo Integer")
   field_float = fields.Float("Campo tipo Float")
   field_select = fields.Selection([('a','A'),('1','uno'),('c','C')],
                   "Campo tipo Selección")
   field_date = fields.Date('Campo tipo fecha')
   field_char = fields.Char("Campo tipo char")
   field_text = fields.Text("Campo tipo Text")
   field_html = fields.Html("Campo tipo HTML")
