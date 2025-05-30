

# Import necessary modules from SQLAlchemy
from sqlalchemy import create_engine  # For creating a database engine
from sqlalchemy.ext.declarative import declarative_base  # For creating base class for models
from sqlalchemy.orm import sessionmaker  # For creating a session factory

# Define the database connection URL
# Format: "mysql+pymysql://username:password@host/database_name"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:franklin@localhost/fastAPI_portfolio"

# Create a database engine
# The engine is responsible for managing connections to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session factory
# SessionLocal will be used to create individual sessions for interacting with the database
# autocommit=False: Disable automatic committing of transactions
# autoflush=False: Disable automatic flushing of changes to the database
# bind=engine: Bind the session factory to the database engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
# All models will inherit from this base class
Base = declarative_base()

# Function to create database tables
def create_tables():
    # Create all tables defined in the models that inherit from Base
    # bind=engine: Use the specified database engine to create the tables
    Base.metadata.create_all(bind=engine)


