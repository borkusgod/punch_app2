from functions_master import *
from datetime import datetime
import json


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

    def create_prof(self):
        f = open('file_write_test.txt', 'x')
        f.write(self.f_name + '\n')
        f.write(self.l_name + '\n')
        f.write(self.crnt_prj + '\n')
        if not self.clock_state:
            f.write("clock state is set to false\n")
        if not self.lunch_state:
            f.write("Lunch state is set to false\n")
        f.close()

        f = open('file_write_test.txt', 'r')
        return f.read()

    def create_prof2(self):
        if not self.clock_state:
            cl_state = "False"
        if not self.lunch_state:
            ln_state = "False"
        dictionary = {
            "first_name": self.f_name,
            "last_name": self.l_name,
            "current_project": self.crnt_prj,
            "clock_state": cl_state,
            "lunch_state": ln_state
        }
        json_object = json.dumps(dictionary, indent=4)

        with open("user_infor2json.json", "w") as outfile:
            outfile.write(json_object)

        with open("user_infor2json.json", "r") as openfile:
            json_object = json.load(openfile)

        print(json_object)
        print(type(json_object))

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
