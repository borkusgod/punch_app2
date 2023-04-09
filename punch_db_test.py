from sqlalchemy import create_engine, DateTime
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

# connect with databases
engine = create_engine('sqlite:///pa_userbase.sqlite', echo=True)

# manage tables
base = declarative_base()


# types you can store in db: String, Numeric, Integer, DateTime
class PunchAppDB(base):
    def __init__(self,
                 emp_id,
                 app_id,
                 f_name,
                 l_name,
                 address,
                 phone_number,
                 email,
                 punch_test):
        self.emp_id = emp_id
        self.app_id = app_id
        self.f_name = f_name
        self.l_name = l_name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.punch_test = punch_test

    __tablename__ = 'PunchAppDB'

    emp_id = Column(Integer, primary_key=True, nullable=False)
    app_id = Column(Integer, nullable=False)
    f_name = Column(String, nullable=False)
    l_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False)
    punch_test = Column(String, nullable=False)


base.metadata.create_all(engine)
