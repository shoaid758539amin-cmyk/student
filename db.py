from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training"
DATABASE_URL="postgresql+psycopg2://training_l3ic_user:vDmK0V90RxLRYIcMuYtruc4ZFNuBQjBL@dpg-dc35cr1ksfps7392o53g-a.oregon-postgres.render.com/training_l3ic"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit = False, autoflush= False, bind=engine)
base = declarative_base()


# def get_connection():
#     db = session_local()
#     try:
#         yield db
#     finally:
#         db.close