from datetime import datetime, time

test_vars = ['7:00', '12:00', '12:30', '16:30']


def punch_in():
    now = datetime.now()
    return f'You punched in at {now}'


def lunch_out():
    now = datetime.now()
    return f'You punched out at {now} for lunch'


def lunch_in():
    now = datetime.now()
    return f'You punched back in at {now} from lunch'


def punch_out():
    now = datetime.now()
    return f'You punched out at {now} for the day'
