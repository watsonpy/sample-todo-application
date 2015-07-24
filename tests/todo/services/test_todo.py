# -*- coding: utf-8 -*-
from todo import services, models


# This would usually be mocked out via unittest.mock
class MockRepository(object):

    def new(self, **kwargs):
        return models.Todo(**kwargs)

    def save(self, model):
        return model


class TestSuiteTodo(object):

    def test_create(self):
        service = services.Todo(MockRepository())
        todo = service.create({'name': 'A Todo'})
        assert todo.name == 'A Todo'

    def test_update(self):
        service = services.Todo(MockRepository())
        todo = service.create({'name': 'A Todo'})
        assert todo.name == 'A Todo'
        todo.name = 'New todo name'
        todo = service.update(todo)
        assert todo.name == 'New todo name'
