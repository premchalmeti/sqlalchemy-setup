import enum

from sqlalchemy import (
    Column, String, Enum, Integer, ForeignKey
)
from sqlalchemy.orm import relationship

from db import BaseModel, DateTimeMixin


class CompanyType(enum.Enum):
    PVT_LTD = 'Pvt. Ltd'
    LLC = 'Llc.'
    LLP = 'Llp.'


class Company(BaseModel):
    __tablename__ = 'companies'

    name = Column(String(length=255))
    users = relationship('User', back_populates='company')
    company_type = Column(Enum(CompanyType))


# class MemberShip(BaseModel):
#     company_id = Column(Integer, ForeignKey('companies.id'))
#     user_id = Column(Integer, ForeignKey('users.id'))
