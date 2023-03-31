# functions used throughout
from datetime import datetime, time

test_vars = ['7:00', '12:00', '12:30', '16:30']


def time_func_args(year, month, day, hour, minute, second):
    ret_date_time = datetime(year, month, day, hour, minute, second)
    return ret_date_time


def name_and_profile():
    get_first = input("What is your first name? ")
    get_last = input("What is your last name? ")
    crt_prj = input("What project are you currently working on? ")
    return get_first, get_last, crt_prj


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
