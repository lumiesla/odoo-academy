#-*- coding:utf-8 -*-
from openerp.osv import fields, osv
class academy_calificacion(osv.osv):
   _name='academy.calificacion'
   _description='Calificaciones de estudiantes'
   _columns={
        'name': fields.many2one('academy.materia', 'Materia'),
       'calificacion': fields.float('Calificacion', digits=(3,2)),
       'student_id':fields.many2one('academy.student','ID Referencia'),
   }
   _defaults={

       }
class academy_materia(osv.osv):
   _name='academy.materia'
   _description='Materias del estudiante'
   _columns={
       'name':fields.char('Nombre')
   }
   _sql_constraints = [('name_uniq', 'unique (name)', 'El nombre de la Materia debe ser unico!'),]