import datetime as dt

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, DateTime, Integer


engine = create_engine(
	'mysql://root:AmazingTheory62@localhost:3306/company', echo=True
)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base(bind=engine)


class DateTimeMixin:
	created_datetime = Column(DateTime, default=dt.datetime.utcnow())
	updated_datetime = Column(
		DateTime, default=dt.datetime.utcnow(),
		onupdate=dt.datetime.utcnow()
	)
	created_datetime._creation_order = 998
	updated_datetime._creation_order = 999


class BaseModel(Base, DateTimeMixin):
	__abstract__ = True

	id = Column(Integer, autoincrement=True, primary_key=True)

	def __str__(self):
		return f'{self.__class__.__name__}(id={self.id})'


def create_all():
	from company import Company
	from user import User
	print(Base.metadata.tables)
	Base.metadata.create_all()
