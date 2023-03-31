# from w3

class Person:
    def __init__(self,
                 f_name,
                 l_name,
                 crnt_prj):
        self.f_name = f_name
        self.l_name = l_name
        self.crnt_prj = crnt_prj

    def myfunc(self):
        print(
            self.f_name + " " + self.l_name + " is currently assigned to the "
                                              "" + self.crnt_prj + " project")

    def punch_in(self):
        print(self.f_name + " has punched in for the morning")

    def punch_in2(self):
        pass

    def lunch_out(self):
        print(self.f_name + " has punched out for lunch time")

    def lunch_in(self):
        print(self.f_name + " has punched back in from lunch")

    def punch_out(self):
        print(self.f_name + " has punched out for the day")
