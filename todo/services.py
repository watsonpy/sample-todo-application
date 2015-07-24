# -*- coding: utf-8 -*-


class Todo(object):
    repository = None

    def __init__(self, repository):
        self.repository = repository

    # Lets assume that more business logic actually occurs in the below methods
    def create(self, todo):
        todo = self.repository.new(**todo)
        return self.repository.save(todo)

    def update(self, todo):
        return self.repository.save(todo)
