# -*- coding: utf-8 -*-
from todo.controllers import Index


# This would usually be mocked out via unittest.mock
class MockRepository(object):

    def all(self):
        return []


class TestSuiteIndex(object):

    def test_get(self):
        # We won't go into mocking out the services here
        index = Index(MockRepository(), 'service')
        assert 'todos' in index.GET()
