# -*- coding: utf-8 -*-
from watson.framework import controllers
from todo import forms


class Base(controllers.Rest):

    """Base controller that abstracts away some common functionality.

    Attibutes:
        todo_repository (todo.repositories.Todo)
        todo_service (todo.services.Todo)
    """
    todo_repository = None
    todo_service = None

    def __init__(self, repository, service):
        self.todo_repository = repository
        self.todo_service = service


class Index(Base):

    """The index view controller is responsible for listing all of the
    Todo items.
    """

    def GET(self):
        """Retrieves a list of todo items.
        """
        return {
            'todos': self.todo_repository.all()
        }


class Todo(Base):

    def GET(self, id=None):
        """Retrieves an individual todo item.

        If a todo already exists we'll 'fake' a PUT method on the form.

        Args:
            id (int): The id of the todo

        Raises:
            If an id is specified and no todo is found, throws a 404
        """
        kwargs = {}
        todo = None
        form_kwargs = {}
        if id:
            todo = self.todo_repository.get(id=id, error_on_not_found=True)
            kwargs = {'id': todo.id}
            form_kwargs['method'] = 'PUT'
        form_kwargs['action'] = self.url('todo', **kwargs)
        form = forms.Todo(**form_kwargs)
        form.bind(todo)

        return {
            'form': form,
            'todo': todo
        }

    def POST(self, **kwargs):
        """Creates a new todo item.
        """
        form = forms.Todo()
        form.data = self.request.post
        if form.is_valid():
            self.todo_service.create({'name': form.data['name']})
            self.flash_messages.add('Created a new todo!', 'success')
        else:
            self.flash_messages.add('You need to enter the todo', 'error')
            return self.redirect('todo')

        return self.redirect('index')

    def PUT(self, id):
        """Updates an existing todo item.

        Args:
            id (int): The id of the todo

        Raises:
            If no todo is found, throws a 404
        """
        todo = self.todo_repository.get(id=id, error_on_not_found=True)
        form = forms.Todo()
        form.bind(todo)
        form.data = self.request.post
        if form.is_valid():
            self.todo_service.update(todo)
            self.flash_messages.add('Updated the todo!', 'success')
        else:
            self.flash_messages.add('Something broke!', 'error')

        return self.redirect(self.url('todo', id=todo.id))

    def DELETE(self, id):
        """Removes a todo item.

        Args:
            id (int): The id of the todo

        Raises:
            If no todo is found, throws a 404
        """
        todo = self.todo_repository.get(id=id, error_on_not_found=True)
        name = todo.name
        self.todo_repository.delete(todo)
        self.flash_messages.add(
            'Deleted the todo "{}"'.format(name), 'success')

        return self.redirect('index')
