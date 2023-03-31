# from w3
from functions_master import *
from datetime import datetime


class Person:
    def __init__(self,
                 f_name='Bill',
                 l_name='Bourque',
                 crnt_prj='Time app',
                 clock_state=False,
                 lunch_state=False):
        self.f_name = f_name
        self.l_name = l_name
        self.crnt_prj = crnt_prj
        self.clock_state = clock_state
        self.lunch_state = lunch_state

    def punch_in(self):
        self.clock_state = True
        time_form = punch_func(2)
        return time_form

    def lunch_out(self):
        print(self.f_name + " has punched out for lunch time")
        self.lunch_state = True
        time_form = punch_func(2)
        return time_form

    def lunch_in(self):
        print(self.f_name + " has punched back in from lunch")
        self.lunch_state = False
        time_form = punch_func(2)
        return time_form

    def punch_out(self):
        print(self.f_name + " has punched out for the day")
        self.clock_state = False
        time_form = punch_func(2)
        return time_form
