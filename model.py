from sqlalchemy import Column,Integer,Float,ForeignKey,String
from database import Base
class CarTypesModel(Base):
    __tablename__ = "car_types"
    car_id = Column(Integer,primary_key=True)
    name = Column(String(50),nullable=False,unique=True)
class CarsModel(Base):
    __tablename__ = "cars"
    id = Column(Integer,primary_key=True)
    car_code = Column(String(10),nullable=False,unique=True)
    rental_price = Column(Float,nullable=False)
    car_type_id = Column(Integer,ForeignKey("car_types.car_id"))