# -*- coding: utf-8 -*-
from todo import models


class TestSuiteTodo(object):

    def test_model(self):
        model = models.Todo()
        model.name = 'Test'
        model.id = 1
        assert model.name == 'Test'
