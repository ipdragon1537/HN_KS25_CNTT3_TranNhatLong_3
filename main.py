from fastapi import FastAPI,Depends,HTTPException,status
from model import CarsModel
from schema import CarResponse,CarCreate
from database import Base,get_db,engine
from sqlalchemy.orm import Session
Base.metadata.create_all(bind=engine)
app = FastAPI()
@app.get("/")
def test():
    return {"message":"test done"}
@app.post("/cars",response_model=CarResponse,status_code=status.HTTP_201_CREATED)
def create_cars(new_car:CarCreate,db:Session = Depends(get_db)):
    new_car = CarsModel(**new_car.model_dump())
    if not new_car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Ko tìm thấy loại xe")
    if db.query(CarsModel).filter(CarsModel.id == new_car.car_code).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Mã xe đã trùng")
    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return new_car
@app.get("/cars",response_model=CarResponse)
def get_all_cars(db:Session = Depends(get_db)):
    list_cars = db.query(CarsModel).all()
    return list_cars
@app.delete("/cars_types/{id}",response_model=CarResponse)
def delete_cars(id:int,db:Session = Depends(get_db)):
    car_delete = db.query(CarsModel).filter(CarsModel.id == id).first()
    if not car_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Không tìm thấy")
    db.delete(car_delete)
    db.commit()




