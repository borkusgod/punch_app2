import database_test
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=database_test.engine)
session = Session()

# all data
for each_q in session.query(database_test.transactions).all():
    print(each_q.transaction_id, each_q.price)

print("*" * 20)
print("Transactions with a price over $40: ")

# selected data
for each_q in session.query(database_test.transactions).filter(
        database_test.transactions.price > 40):
    print(each_q.transaction_id, each_q.price)
