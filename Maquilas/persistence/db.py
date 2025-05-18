from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONNECTION = 'mysql+pymysql://root:guzman@localhost:3308/maquilas'
SessionLocal = sessionmaker(bind = create_engine(CONNECTION, echo = False))