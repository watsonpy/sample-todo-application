# -*- coding: utf-8 -*-
from watson.form import Form, fields
from watson import validators


class Todo(Form):
    name = fields.Text(label='Name', validators=[validators.Required()])
    submit = fields.Submit(value='Save', button_mode=True)
