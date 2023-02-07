from sqlalchemy import create_engine
from config.env_variables import DATABASE_URL , DEBUG_MODE
from sqlalchemy.ext.declarative  import declarative_base


Engine = create_engine(DATABASE_URL, echo=DEBUG_MODE)

Base = declarative_base()


