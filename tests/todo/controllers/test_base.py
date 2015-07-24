# -*- coding: utf-8 -*-
from todo.controllers import Base


class TestSuiteBase(object):

    def test_instantiate(self):
        # We won't go into mocking out the services here
        base = Base('repo', 'service')
        assert base.todo_repository == 'repo'
