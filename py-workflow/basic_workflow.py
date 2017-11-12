#!/bin/python

import random
from workflow.engine import GenericWorkflowEngine
from functools import wraps
from workflow.errors import HaltProcessing
from workflow.patterns.controlflow import (
FOR,        # Simple for-loop, a-la python. First argument is an iterable,
            # second defines where to save the current value, and the third
            # is the code that runs in the loop.

HALT,       # Halts the engine. This brings it to a state where it can be
            # inspected, resumed, restarted, or other.

IF_ELSE,    # Simple `if-else` statement that accepts 3 arguments.
            # (condition, tasks if true, tasks if false)

CMP,        # Simple function to support python comparisons directly from a
            # workflow engine.
WHILE,
)

def print_data(obj, eng):
    """Print the data found in the token."""
    print obj.data

def add_data(number_to_add):
    """Add number_to_add to obj.data."""
    @wraps(add_data)
    def _add_data(obj, eng):
        obj.data += number_to_add
    return _add_data

def append_from(key):
    """Append data from a given `key` of the engine's `extra_data`."""
    def _append_from(obj, eng):
        obj.append(eng.extra_data[key])
        print "new data:", obj
    return _append_from

def append_random():
    def _append_random(obj, eng):
        obj.append(random.randint(1, 100))
        print "new data:", obj
    return _append_random

def interrupt_workflow(obj, eng):
    """Raise the `HaltProcessing` exception.

    This is not handled by the engine and bubbles up to our code.
    """
    print "Raising HaltProcessing"
    eng.halt("interrupting this workflow.")

def restart_workflow(obj, eng):
    """Restart the engine with the current object, from the first task."""
    print "Restarting the engine"
    eng.restart('current', 'first')

my_workflow_1 = [
    add_data(1),
    print_data
]

my_workflow_2 = [
    FOR(range(2), "my_current_value", # For-loop, from 0 to 1, that sets
                                      # the current value to
                                      # `eng.extra_data["my_current_value"]`
        [
            append_from("my_current_value"),  # Gets the value set above
                                              # and appends it to our token
        ]
    ), # END FOR

    # IF_ELSE(
    #     CMP((lambda o, e: o), [0, 1 ,0, 1], "<"),  # Condition:
    #                                                # "if obj < [0,1,0,1]:"

    #     [ restart_workflow ],                   # Tasks to run if condition
    #                                             # is True:
    #                                             # "return back to the FOR"

    #     [                                       # Tasks to run if condition
    #                                             # is False:

    #     append_from("my_current_value"),        # "append 1 (note we still
    #                                             # have access to it)
    #     interrupt_workflow                      # and interrupt"
    #     ]
    # ) # END IF_ELSE
]

my_workflow_3 = [
    FOR(range(5), 'tmp', [append_random()])
    #WHILE(isinstance("key",int), [append_random()])
]

class MyObject(object):
    def __init__(self, data):
        self.data = data

def run_workflow_1():
	my_object0 = MyObject(0)
	my_object1 = MyObject(1)

	my_engine_1 = GenericWorkflowEngine()
	my_engine_1.setWorkflow(my_workflow_1)

	my_engine_1.process([my_object0, my_object1])


def run_workflow_2():
	# Create the engine as in the previous example
	my_engine_2 = GenericWorkflowEngine()
	my_engine_2.setWorkflow(my_workflow_2)

	try:
	    # Note how we don't need to keep a reference to our tokens - the engine
	    # allows us to access them via `my_engine.objects` later.
	    my_engine_2.process([[], [0,1], [0,1,0,1]])
	except HaltProcessing:
	    # Our engine was built to throw this exception every time an object is
	    # completed. At this point we can inspect the object to decide what to
	    # do next. In any case, we will ask it to move to the next object,
	    # until it stops throwing the exception (which, in our case, means it
	    # has finished with all objects).
	    while True:
	        try:
	            # Restart the engine with the next object, starting from the
	            # first task.
	            my_engine_2.restart('next', 'first')
	        except HaltProcessing:
	            continue
	        else:
	            print "Done!", my_engine_2.objects
	            break

def run_workflow_3():
    my_engine_3 = GenericWorkflowEngine()
    my_engine_3.setWorkflow(my_workflow_3)
    my_engine_3.process([[]])

def main():
	run_workflow_3()

if __name__ == '__main__':
	main()