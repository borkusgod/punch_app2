import database_test
from sqlalchemy.orm import sessionmaker
import random

# new session
Session = sessionmaker(bind=database_test.engine)
session = Session()

# adding random data
for each in range(10, 20):
    item_id = random.randint(0, 1000)
    price = random.randint(20, 50)

    tr = database_test.transactions(each, '2023/04/08', item_id, price)
    session.add(tr)

# save changes in the database
session.commit()
