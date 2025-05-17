from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONNECTION = 'mysql+pymysql://root:jrcz2005@localhost/pinata'
SessionLocal = sessionmaker(bind = create_engine(CONNECTION, echo = False))
