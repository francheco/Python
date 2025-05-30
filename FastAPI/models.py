

# Import necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table  # For defining table columns
from sqlalchemy.orm import relationship  # For defining relationships between tables
from database import Base  # Import the Base class for declarative models

# Define the Course model (represents the "courses" table)
class Course(Base):
    __tablename__ = "courses"  # Name of the table in the database

    # Define the columns for the "courses" table
    id = Column(Integer, primary_key=True, index=True)  # Primary key, auto-incremented
    subject = Column(String(255), nullable=False)  # Subject of the course (cannot be null)
    title = Column(String(255), nullable=False)  # Title of the course (cannot be null)
    description = Column(Text)  # Description of the course (can be null)

# Define the User model (represents the "users" table)
class User(Base):
    __tablename__ = "users"  # Name of the table in the database

    # Define the columns for the "users" table
    id = Column(Integer, primary_key=True, index=True)  # Primary key, auto-incremented
    name = Column(String(255), nullable=False)  # Name of the user (cannot be null)
    email = Column(String(255), unique=True, nullable=False)  # Email of the user (must be unique and cannot be null)

    # Define a many-to-many relationship between users and courses
    # "secondary" specifies the association table for the relationship
    # "backref" creates a reverse relationship from Course to User
    courses = relationship("Course", secondary="user_courses", backref="users")

# Define the User-Courses association table
# This table links users to courses in a many-to-many relationship
user_courses = Table(
    "user_courses",  # Name of the table in the database
    Base.metadata,  # Use the metadata from the Base class

    # Define the columns for the "user_courses" table
    Column("user_id", Integer, ForeignKey("users.id")),  # Foreign key to the "users" table
    Column("course_id", Integer, ForeignKey("courses.id"))  # Foreign key to the "courses" table
)


