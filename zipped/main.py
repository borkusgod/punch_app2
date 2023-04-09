# this will be an app to replicate what is being made by Mobile+Web in
# Android. The idea is to concept and deploy for the practice

from functions_master import *
from classes import *
from testing_vars_module import *
from text_module import *

begin = first_run()

if begin:
    print(greeting)
    p1 = Person()  # using test vars
print('Print test output below\n\n')
print(f'First name is: {p1.f_name}\n'
      f'Last name is: {p1.l_name}\n'
      f'Current project is: {p1.crnt_prj}')
morn_punch = p1.punch_in()
lunch_out = p1.lunch_out()
lunch_in = p1.lunch_in()
after_out = p1.punch_out()
print(morn_punch)
print(lunch_out)
print(lunch_in)
print(after_out)

crt_prf = p1.create_prof()
print(crt_prf)

json_ex = p1.create_prof2()
