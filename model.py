from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date


Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def __repr__(self):
        return "<Person(id={}, first_name='{}', last_name='{}')>"\
            .format(self.id, self.first_name, self.last_name)