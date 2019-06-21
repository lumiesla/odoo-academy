#-*- coding:utf-8 -*-
from openerp import models, fields, api

class academy_student(models.Model):
    _name='academy.student'
    _description='modelo de formulario para estudiante'
    name=fields.Char('Nombre', size=128)
    last_name=fields.Char('Apellido', size=128)
    photo=fields.Binary('Fotografía')
    create_date=fields.Datetime('Fecha Creación', readonly=True)
        