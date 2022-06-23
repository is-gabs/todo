from src.backends.sql_database.database import _get_engine
from src.backends.sql_database.model import Base

if __name__ == '__main__':
    Base.metadata.create_all(_get_engine())
