import punch_db_test
from sqlalchemy.orm import sessionmaker
import random

with open("names_list.txt") as file_read:
    name_file = file_read.readlines()
    len_of_nf = len(name_file)


def rand_gen():
    r_out = random.randint(0, len_of_nf)
    return r_out


def rand_phone():
    area = str(random.randint(100, 999))
    ext = str(random.randint(100, 999))
    last4 = str(random.randint(1000, 9999))
    number_out = f'({area}) {ext}-{last4}'
    return number_out


# new session
Session = sessionmaker(bind=punch_db_test.engine)
session = Session()

# adding random data
for each in range(10, 20):
    emp_id = random.randint(0, 1000)
    app_id = random.randint(0, 500)
    get_rand = rand_gen()
    f_name = name_file[get_rand]
    l_name = name_file[get_rand]
    address = "555 Hill Road, China, ME 99999"
    phone_number = rand_phone()
    email = "test_email@gmail.com"
    punch_test = "Placeholder"

    tr = punch_db_test.PunchAppDB(emp_id,
                                  app_id,
                                  f_name,
                                  l_name,
                                  address,
                                  phone_number,
                                  email,
                                  punch_test)
    session.add(tr)

# save changes in the database
session.commit()
