# -*- coding: utf-8 -*-
from io import BytesIO, BufferedReader
from watson.http import messages
from todo.controllers import Todo
from todo.app import application
from todo import models


# This would usually be mocked out via unittest.mock
class MockRepository(object):
    models = None

    def __init__(self):
        self.models = []

    def get(self, id, error_on_not_found=True):
        for model in self.models:
            if model.id == id:
                return model
        return None

    def new(self, data):
        model = models.Todo(**data)
        model.id = 1
        self.models.append(model)
        return model

    def delete(self, id):
        pass


class MockService(object):

    def __init__(self, repository):
        self.repository = repository

    def create(self, data):
        return self.repository.new(data)

    def update(self, model):
        return self.repository.get(model.id)


class TestSuiteTodo(object):

    def setup(self):
        repo = MockRepository()
        service = MockService(repo)
        self.controller = Todo(repo, service)
        self.controller.container = application.container
        data = 'name=Testing'
        environ = {'REQUEST_METHOD': 'POST', 'CONTENT_LENGTH': len(data)}
        environ['wsgi.input'] = BufferedReader(BytesIO(data.encode('utf-8')))
        request = messages.Request.from_environ(
            environ,
            session_class='watson.http.sessions.Memory')
        self.controller.request = request

    def test_get(self):
        # We won't go into mocking out the services here
        self.controller.todo_repository.new({'name': 'Test'})
        assert 'todo' in self.controller.GET()
        assert self.controller.GET(1)['todo'].name == 'Test'

    def test_post(self):
        post = self.controller.POST()
        assert post.status_code == 303
        model = self.controller.todo_repository.get(1)
        assert model.name == 'Testing'

    def test_put(self):
        self.controller.todo_repository.new({'name': 'Test'})
        assert self.controller.todo_repository.get(1).name == 'Test'
        put = self.controller.PUT(1)
        assert put.status_code == 303
        model = self.controller.todo_repository.get(1)
        assert model.name == 'Testing'

    def test_delete(self):
        self.controller.todo_repository.new({'name': 'Test'})
        response = self.controller.DELETE(1)
        assert response.status_code == 303
