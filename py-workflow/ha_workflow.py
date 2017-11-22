#!/bin/python

from workflow.patterns.controlflow import IF, HALT
from workflow.engine import HaltProcessing, TransitionActions
from workflow.engine_db import (
    DbWorkflowEngine,
    ObjectStatus,
    WorkflowStatus,
    DbProcessingFactory,
)
from workflow.utils import classproperty
import random, mock

class Grade(object):
    def __init__(self, data):
        self.id = random.randint(10000, 99999);
        self.data = data

def grade_is_not_passing(obj, eng):
    print 'Testing grade #{0}, with data {1}'.format(obj.id, obj.data)
    return obj.data < 5

callbacks = [
    IF(grade_is_not_passing,
        [
            HALT()
        ]),
]

class DummyDbObj(object):
    def __init__(self):
        self._status = None

    def save(self, status):
        pass

    @property
    def uuid(self):
        pass

    @property
    def name(self):
        pass

    @property
    def status(self):
        return self._status

    @property
    def objects(self):
        pass

Global_Array = []
dummy_db_obj = mock.Mock(spec=DummyDbObj())
dummy_db_obj.save(WorkflowStatus.NEW)
my_db_engine = DbWorkflowEngine(dummy_db_obj)
my_db_engine.callbacks.replace(callbacks)
try:
    data = ['one', 'two', 'three', 'four', 'five']
    my_db_engine.process(data)
except HaltProcessing:
    print 'The student has failed this test!'