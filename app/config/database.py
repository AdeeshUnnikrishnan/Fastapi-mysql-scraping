from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


host = "localhost"
user = "root"
password = "Qwertyuiop7502755701"
database_name = 'bse'
table_name = 'bsecraped'
DATABASE_URL = f'mysql+pymysql://{user}:{password}@{host}:3307/{database_name}'
def db_connect(df):
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:3307/{database_name}')
    print("connected")
    # Specify the name of the table in your MySQL database
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print("added")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()