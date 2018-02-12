import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Insurance(Base):
    __tablename__ = 'insurance'

    id = Column(Integer, primary_key=True)
    name = Column(String(90), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    insurance_fields = relationship('InsuranceField', cascade='all, delete-orphan')
# We added this serialize function to be able to send JSON objects in a
# serializable format

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class InsuranceField(Base):
    __tablename__ = 'insurance_field'

    name = Column(String(90), nullable=False)
    id = Column(Integer, primary_key=True)
    Address = Column(String(300))
    # Date = Column(String(20))
    InsuredValue = Column(String(20))
    Type = Column(String(10))
    # Model = Column(String(10))
    insurance_id = Column(Integer, ForeignKey('insurance.id'))
    insurance = relationship(Insurance)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

# We added this serialize function to be able to send JSON objects in a
# serializable format
    @property
    def serialize(self):

        return {
            'name': self.name,
            'Address': self.Address,
            'id': self.id,
            'InsuredValue': self.InsuredValue,
            'Type': self.Make,
            'Model': self.Model,
            'Date': self.Date,
        }


#engine = create_engine('sqlite:///restaurantmenu.db')
engine = create_engine('sqlite:///insuranceBritecore.db')
Base.metadata.create_all(engine)
