from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# 1. Define your Database URL
# Format: postgresql://username:password@localhost:5432/db_name
DATABASE_URL = "postgresql://postgres:your_password@localhost:5432/zevo_db"

# 2. Create the Engine
engine = create_engine(DATABASE_URL)

# 3. Create a Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Create the Base class for Models
Base = declarative_base()

# 5. Dependency to get DB session in routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
