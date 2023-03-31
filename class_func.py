import class_test
import functions_pyc

create_profile = functions_pyc.name_and_profile()
p1 = class_test.Person(
    create_profile[0], create_profile[1], create_profile[2]
)

p1.myfunc()
p1.punch_in()
p1.lunch_out()
p1.lunch_in()
p1.punch_out()
