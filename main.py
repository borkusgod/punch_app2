# this will be an app to replicate what is being made by Mobile+Web in
# Android. The idea is to concept and deploy for the practice

from functions_master import *
from class_test import *
from testing_vars_module import *
import text_module

# testing variables

f_info = get_full_name()
p1 = Person(f_info[0], f_info[1], f_info[2])
first_punch = p1.punch_in()
if first_punch:
    print('You are punched in')
