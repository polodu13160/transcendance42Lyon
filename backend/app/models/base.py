from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.env import DATABASE_URL

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    pass


