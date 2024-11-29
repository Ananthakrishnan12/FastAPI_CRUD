from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Your MySQL database URL
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:tensorflow97@localhost/fastapi_db"  # Modify this with your actual credentials

# Create engine for MySQL (no need for check_same_thread for MySQL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
