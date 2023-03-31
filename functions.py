from datetime import datetime

# format year,month,day,hour, minute,second


test_vars = ['7:00', '12:00', '12:30', '16:30']


def punch_in():
    now = datetime.now()
    # test_pun_in = time(11, 34, 56)
    time = now.strftime("%I:%M %p")
    return f'You punched in at {time}'


def lunch_out():
    now = datetime.now()
    time = now.strftime("%I:%M %p")
    return f'You punched out at {time} for lunch'


def lunch_in():
    now = datetime.now()
    time = now.strftime("%I:%M %p")
    return f'You punched back in at {time} from lunch'


def punch_out():
    now = datetime.now()
    time = now.strftime("%I:%M %p")
    return f'You punched out at {time} for the day'
