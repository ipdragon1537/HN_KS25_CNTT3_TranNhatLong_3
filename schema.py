from pydantic import BaseModel,Field
from typing import Optional
class CarCreate(BaseModel):
    car_code:str = Field(...,min_length=4,max_length=10)
    rental_price :int = Field(gt=0)
    car_type_id:int 
class CarResponse(BaseModel):
    id:int
    car_code:str
    rental_price:float
    class Config:
        from_attribute:True