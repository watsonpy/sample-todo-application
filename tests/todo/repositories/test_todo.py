# -*- coding: utf-8 -*-
from todo.repositories import Todo


class TestSuiteTodo(object):

    def test_instantiate(self):
        assert Todo('dummy_session')
