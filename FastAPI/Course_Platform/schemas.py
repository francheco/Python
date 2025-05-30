

# Import necessary modules from Pydantic
from pydantic import BaseModel, EmailStr  # BaseModel for schema definition, EmailStr for email validation

# Course Schemas

# Base schema for Course (used for common fields)
class CourseBase(BaseModel):
    subject: str  # Subject of the course
    title: str  # Title of the course
    description: str  # Description of the course

# Schema for creating a Course (inherits from CourseBase)
class CourseCreate(CourseBase):
    pass  # No additional fields, same as CourseBase

# Schema for returning a Course (inherits from CourseBase)
class Course(CourseBase):
    id: int  # Add the course ID (primary key)

    # Pydantic configuration
    class Config:
        orm_mode = True  # Enable ORM mode to allow parsing from SQLAlchemy models

# User Schemas

# Base schema for User (used for common fields)
class UserBase(BaseModel):
    name: str  # Name of the user
    email: EmailStr  # Email of the user (validated using EmailStr)

# Schema for creating a User (inherits from UserBase)
class UserCreate(UserBase):
    pass  # No additional fields, same as UserBase

# Schema for returning a User (inherits from UserBase)
class User(UserBase):
    id: int  # Add the user ID (primary key)

    # Pydantic configuration
    class Config:
        orm_mode = True  # Enable ORM mode to allow parsing from SQLAlchemy models

# User-Courses Relationship Schema

# Schema for linking a user to a course
class UserCourses(BaseModel):
    user_id: int  # ID of the user
    course_id: int  # ID of the course
