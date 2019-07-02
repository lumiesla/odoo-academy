#-*- coding:utf-8 -*-
from openerp import models, fields, api

class res_partner(models.Model):
  _name='res.partner'
  _inherit='res.partner'
  company_type = fields.Selection([('person', 'Individual'),
                    ('company', 'Compañia'),
                    ('is_school','Escuela')
                    # ('student','Estudiante')
                    ],
         string='Company Type',
         help='Technical field, used only to display a boolean using a radio '
              'button. As for Odoo v9 RadioButton cannot be used on boolean '
              'fields, this one serves as interface. Due to the old API '
              'limitations with interface function field, we implement it '
              'by hand instead of a true function field. When migrating to '
              'the new API the code should be simplified.')
    # student_id = fields.Many2one('academy.student', 'Estudiante')        
class academy_student(models.Model):
  _name='academy.student'
  _description='modelo de formulario para estudiante'
  name=fields.Char('Nombre', size=128)
  last_name=fields.Char('Apellido', size=128, required=True)
  photo=fields.Binary('Fotografía')
  create_date=fields.Datetime('Fecha Creación', readonly=True)
  notes=fields.Html('Comentarios')
  active=fields.Boolean('Activo')
  state = fields.Selection([('draft','Documento Borrador'),
                           ('progress','Progeso'),
                           ('done','Egresado'),], 'Estado',default="draft")
  # age=fields.Integer('Edad', required=True)
  partner_id = fields.Many2one('res.partner','Escuela')
  calificaciones_ids = fields.One2many('academy.calificacion','student_id','Calificaciones')


   #_order = 'name'
    
   #_defaults={
   #    'active':True,
   #    'state':'draft',
   # }    