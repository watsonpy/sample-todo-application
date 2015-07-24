# -*- coding: utf-8 -*-
from watson.framework import events

debug = {
    'enabled': True
}

dependencies = {
    'definitions': {
        'todo_repository': {
            'item': 'todo.repositories.Todo',
            'init': ['sqlalchemy_session_default']
        },
        'todo_service': {
            'item': 'todo.services.Todo',
            'init': ['todo_repository']
        },
        'index_controller': {
            'item': 'todo.controllers.Index',
            'init': {
                'repository': 'todo_repository',
                'service': 'todo_service'
            }
        },
        'todo_controller': {
            'item': 'todo.controllers.Todo',
            'init': {
                'repository': 'todo_repository',
                'service': 'todo_service'
            }
        }
    }
}

db = {
    'connections': {
        'default': {
            'connection_string': 'sqlite:///../data/todo.sqlite',
            'metadata': 'todo.models.Model'
        }
    }
 }

events = {
    events.INIT: [
       ('watson.db.listeners.Init', 1, True)
    ],
}

routes = {
    'index': {
        'path': '/',
        'options': {'controller': 'index_controller'}
    },
    'todo': {
        'path': '/todo[/:id]',
        'options': {'controller': 'todo_controller'}
    }
}
