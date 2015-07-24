# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import Column, Integer, DateTime, String
from watson.db.models import Model


class Todo(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    created = Column(DateTime, default=datetime.datetime.utcnow)
