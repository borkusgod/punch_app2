# functions used throughout
from datetime import datetime
import os.path
from text_module import *


def first_run():
    path = './app_first_run.txt'
    if not os.path.isfile(path):
        with open('app_first_run.txt', 'w') as fr_write:
            fr_write.write(fr_header)
    else:
        print("App has been run before")


def time_func_args(year, month, day, hour, minute, second):
    ret_date_time = datetime(year, month, day, hour, minute, second)
    return ret_date_time


def get_full_name():
    gt_fname = input('Please type in your first name: \n')
    gt_lname = input('Please type in your last name: \n')
    asg_prj = input('Please type in the project that you are assigned to: \n')
    return gt_fname, gt_lname, asg_prj


def punch_in():
    now = datetime.now()
    time_form = now.strftime("%I:%M %p")
    # return f'You punched in at {time_form} this morning.'
    return time_form


def punch_func(from_func):
    punch_time = datetime.now()
    x = from_func
    time_form = punch_time.strftime("%I:%M %p")
    return time_form


def punch_in2():
    print('punch in')


def lunch_out():
    return 'You have punched out for lunch'


def lunch_in():
    return 'You have punched back in from taking a lunch'


def punch_out():
    return 'You have punched out for the day'


def add(a, b):
    return a + b