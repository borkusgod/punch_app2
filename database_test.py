from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

# connect with databases
engine = create_engine('sqlite:///sqlalchemy.sqlite', echo=True)

# manage tables
base = declarative_base()


class transactions(base):
    def __init__(self, transaction_id, date, item_id, price):
        self.transaction_id = transaction_id
        self.date = date
        self.item_id = item_id
        self.price = price
    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True)
    date = Column(String)
    item_id = Column(Integer)
    price = Column(Integer)

# this was originally here but it gave a type error on run
# left here as comment for that reason
# def __init__(self, transaction_id, date, item_id, price):
#     self.transaction_id = transaction_id
#     self.date = date
#     self.item_id = item_id
#     self.price = price


base.metadata.create_all(engine)
