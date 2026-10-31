from sqlalchemy.orm import sessionmaker,declarative_base,Session
from sqlalchemy import create_engine
URL = "mysql+pymysql://root:123456@localhost:3306/car_rental_db"
engine = create_engine(URL)
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit = False)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()