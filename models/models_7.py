#-*- coding:utf-8 -*-
from openerp.osv import field, osv
class academy_calificacion(osv.osv):
    _name='academy.calificacion'
    _description='Calificaciones de estudiantes'
    _columns={
        'name':fields.many2one('academy.materia','Materia')
        'calificacion':fields.float('Calificación', digits=(3,2))
    }
    _defaults={

        }
class academy_materia(osv.osv):
    _name='academy.materia'
    _description='Materias del estudiante'
    _columns={
        'name':fields.char('Nombre')
    }
    _defaults={

        }