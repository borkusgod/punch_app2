# for classes
import functions_pyc


class Employee:
    def __init__(self, name):
        self.name = name


class PunchClass:
    def __init__(self, name):
        self.name = name

    def punch_in(self):
        print(self.name + " punched in")

    def lunch_out(self):
        print(self.name + " punched out for lunch.")

    def lunch_in(self):
        print(self.name + " punched back in from lunch.")

    def punch_out(self):
        print(self.name + " punched out for the day.")


get_name = input("Please enter your name: ")
p1 = PunchClass(get_name)
p1.punch_in()
