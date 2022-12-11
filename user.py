import enum

from sqlalchemy import Column, String, DateTime, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship

from db import BaseModel, DateTimeMixin


class UserRoles(enum.Enum):
	EMPLOYEE = 'Emp'
	MANAGER = 'Mgr'
	DEVELOPER = 'Dev'


class User(BaseModel):
    __tablename__ = 'users'

    name = Column(String(50))
    # email = Column(String(255), unique=True, index=True, nullable=False)
    role = Column(Enum(UserRoles))
    company_id = Column(Integer, ForeignKey('companies.id'))

    company = relationship('Company', back_populates='users')


# class Employee(User):
# 	__mapper_args__ = {
# 		'polymorphic_identity_on': 'role',
# 		'polymorphic_identity_type': 'Emp'
# 	}

