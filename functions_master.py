# functions used throughout
from datetime import datetime, time


def time_func_args(year, month, day, hour, minute, second):
    ret_date_time = datetime(year, month, day, hour, minute, second)
    return ret_date_time

# this is now redundant because it will be worked into the class
# def name_and_profile():
#     get_first = input("What is your first name? ")
#     get_last = input("What is your last name? ")
#     crt_prj = input("What project are you currently working on? ")
#     return get_first, get_last, crt_prj


def get_full_name():
    gt_fname = input('Please type in your first name: \n')
    gt_lname = input('Please type in your last name: \n')
    asg_prj = input('Please type in the project that you are assigned to: \n')
    return gt_fname, gt_lname, asg_prj


def punch_in():
    now = datetime.now()
    time_form = now.strftime("%I:%M %p")
    return f'You punched in at {time_form} this morning.'


def punch_in2():
    print('punch in')


def lunch_out():
    return 'You have punched out for lunch'


def lunch_in():
    return 'You have punched back in from taking a lunch'


def punch_out():
    return 'You have punched out for the day'
