

from sqlalchemy.orm import Session  # Import Session for database interactions
import models  # Import the SQLAlchemy models
import schemas  # Import the Pydantic schemas

# Create a new course
def create_course(db: Session, course: schemas.CourseCreate):
    # Convert the Pydantic schema to a dictionary and unpack it into the Course model
    db_course = models.Course(**course.dict())
    # Add the new course to the database session
    db.add(db_course)
    # Commit the transaction to save the course in the database
    db.commit()
    # Refresh the instance to get the updated data (e.g., auto-generated ID)
    db.refresh(db_course)
    # Return the newly created course
    return db_course

# Get a course by ID
def get_course(db: Session, course_id: int):
    # Query the database for the course with the given ID
    return db.query(models.Course).filter(models.Course.id == course_id).first()

# Get all courses
def get_courses(db: Session, skip: int = 0, limit: int = 100):
    # Query the database for all courses, with pagination (skip and limit)
    return db.query(models.Course).offset(skip).limit(limit).all()

# Update a course
def update_course(db: Session, course_id: int, course: schemas.CourseCreate):
    # Query the database for the course with the given ID
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if db_course:
        # Update the course attributes with the new values
        db_course.subject = course.subject
        db_course.title = course.title
        db_course.description = course.description
        # Commit the transaction to save the changes
        db.commit()
        # Refresh the instance to get the updated data
        db.refresh(db_course)
    # Return the updated course
    return db_course

# Delete a course
def delete_course(db: Session, course_id: int):
    # Query the database for the course with the given ID
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if db_course:
        # Delete the course from the database session
        db.delete(db_course)
        # Commit the transaction to remove the course from the database
        db.commit()
    # Return the deleted course
    return db_course

# Create a new user
def create_user(db: Session, user: schemas.UserCreate):
    # Convert the Pydantic schema to a dictionary and unpack it into the User model
    db_user = models.User(**user.dict())
    # Add the new user to the database session
    db.add(db_user)
    # Commit the transaction to save the user in the database
    db.commit()
    # Refresh the instance to get the updated data (e.g., auto-generated ID)
    db.refresh(db_user)
    # Return the newly created user
    return db_user

# Get a user by ID
def get_user(db: Session, user_id: int):
    # Query the database for the user with the given ID
    return db.query(models.User).filter(models.User.id == user_id).first()

# Get all users
def get_users(db: Session, skip: int = 0, limit: int = 100):
    # Query the database for all users, with pagination (skip and limit)
    return db.query(models.User).offset(skip).limit(limit).all()

# Update a user
def update_user(db: Session, user_id: int, user: schemas.UserCreate):
    # Query the database for the user with the given ID
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        # Update the user attributes with the new values
        db_user.name = user.name
        db_user.email = user.email
        # Commit the transaction to save the changes
        db.commit()
        # Refresh the instance to get the updated data
        db.refresh(db_user)
    # Return the updated user
    return db_user

# Delete a user
def delete_user(db: Session, user_id: int):
    # Query the database for the user with the given ID
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        # Delete the user from the database session
        db.delete(db_user)
        # Commit the transaction to remove the user from the database
        db.commit()
    # Return the deleted user
    return db_user

# Add a course to a user
def add_user_to_course(db: Session, user_id: int, course_id: int):
    # Query the database for the user with the given ID
    user = db.query(models.User).filter(models.User.id == user_id).first()
    # Query the database for the course with the given ID
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if user and course:
        # Add the course to the user's list of courses
        user.courses.append(course)
        # Commit the transaction to save the relationship
        db.commit()
        # Return the updated user
        return user
    # Return None if the user or course doesn't exist
    return None

# Get all courses for a user
def get_user_courses(db: Session, user_id: int):
    # Query the database for the user with the given ID
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        # Return the list of courses associated with the user
        return user.courses
    # Return None if the user doesn't exist
    return None

# Remove a course from a user
def remove_user_from_course(db: Session, user_id: int, course_id: int):
    # Query the database for the user with the given ID
    user = db.query(models.User).filter(models.User.id == user_id).first()
    # Query the database for the course with the given ID
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if user and course:
        # Remove the course from the user's list of courses
        user.courses.remove(course)
        # Commit the transaction to remove the relationship
        db.commit()
        # Return the updated user
        return user
    # Return None if the user or course doesn't exist
    return None
