# -*- coding: utf-8 -*-
from watson.db import repositories
from todo import models


class Todo(repositories.Base):
    __model__ = models.Todo
