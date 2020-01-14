from odoo import models, fields, api

class Book(models.Model):
#   _inherit = 'sale.order'
   _name = 'prueba.book'

   name = fields.Char("Book")
   active = fields.Boolean("Active")
   image = fields.Html("Image")
   pages = fields.Integer("Pages")
   isbn = fields.Char("Ibsn")
   category_id = fields.Many2one('prueba.category',string="Category", 
                  index=True,ondelete='set null')
#   category_ids = fields.One2many('prueba.category','id')
  
class Category(models.Model):
   _name = 'prueba.category'

   name = fields.Char("Category")
   active = fields.Boolean("Active")
