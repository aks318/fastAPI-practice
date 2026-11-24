from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from sqlalchemy import create_engine
from sqlalchemy.engine import URL

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg",
    username="aakash",
    password="Aakash@123",
    host="localhost",
    port=5432,
    database="chatbot"
)

engine = create_engine(DATABASE_URL)

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()