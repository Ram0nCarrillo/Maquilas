from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONNECTION = 'mysql+pymysql://root:jrcz2005@127.0.0.1:3306/maquilas'

SessionLocal = sessionmaker(bind=create_engine(CONNECTION, echo=False))
