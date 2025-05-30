
# Import necessary modules from FastAPI and SQLAlchemy
from fastapi import FastAPI, Depends, HTTPException  # FastAPI framework and dependencies
from sqlalchemy.orm import Session  # For database session management
import models, schemas, crud  # Import models, schemas, and CRUD functions
from database import SessionLocal, engine, create_tables  # Import database-related functions

# Create a FastAPI application instance
app = FastAPI()

# Create database tables
# This ensures that all tables defined in the models are created in the database
create_tables()

# Dependency to get a database session
def get_db():
    # Create a new database session
    db = SessionLocal()
    try:
        # Yield the session to the endpoint function
        yield db
    finally:
        # Close the session after the request is complete
        db.close()

# Root endpoint
@app.get("/")
def read_root():
    # Return a simple message for the root endpoint
    return {"message": "I am Franklin and this is my project to learn FastAPI!"}

# Test database connection endpoint
@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    # Return a message to confirm the database connection is working
    return {"message": "Database connection successful!"}

# Course Endpoints

# Create a new course
@app.post("/courses/", response_model=schemas.Course)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    # Call the CRUD function to create a course
    return crud.create_course(db, course)

# Get a course by ID
@app.get("/courses/{course_id}", response_model=schemas.Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    # Call the CRUD function to get a course by ID
    db_course = crud.get_course(db, course_id)
    # If the course doesn't exist, raise a 404 error
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    # Return the course
    return db_course

# Get all courses
@app.get("/courses/", response_model=list[schemas.Course])
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Call the CRUD function to get all courses with pagination
    return crud.get_courses(db, skip=skip, limit=limit)

# Update a course
@app.put("/courses/{course_id}", response_model=schemas.Course)
def update_course(course_id: int, course: schemas.CourseCreate, db: Session = Depends(get_db)):
    # Call the CRUD function to update a course
    db_course = crud.update_course(db, course_id, course)
    # If the course doesn't exist, raise a 404 error
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    # Return the updated course
    return db_course

# Delete a course
@app.delete("/courses/{course_id}", response_model=schemas.Course)
def delete_course(course_id: int, db: Session = Depends(get_db)):
    # Call the CRUD function to delete a course
    db_course = crud.delete_course(db, course_id)
    # If the course doesn't exist, raise a 404 error
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    # Return the deleted course
    return db_course

# User Endpoints

# Create a new user
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Call the CRUD function to create a user
    return crud.create_user(db, user)

# Get a user by ID
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    # Call the CRUD function to get a user by ID
    db_user = crud.get_user(db, user_id)
    # If the user doesn't exist, raise a 404 error
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    # Return the user
    return db_user

# Get all users
@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Call the CRUD function to get all users with pagination
    return crud.get_users(db, skip=skip, limit=limit)

# Update a user
@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Call the CRUD function to update a user
    db_user = crud.update_user(db, user_id, user)
    # If the user doesn't exist, raise a 404 error
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    # Return the updated user
    return db_user

# Delete a user
@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    # Call the CRUD function to delete a user
    db_user = crud.delete_user(db, user_id)
    # If the user doesn't exist, raise a 404 error
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    # Return the deleted user
    return db_user

# User-Courses Endpoints

# Add a course to a user
@app.post("/users/{user_id}/courses/{course_id}", response_model=schemas.User)
def add_course_to_user(user_id: int, course_id: int, db: Session = Depends(get_db)):
    # Call the CRUD function to add a course to a user
    return crud.add_user_to_course(db, user_id, course_id)

# Get all courses for a user
@app.get("/users/{user_id}/courses/", response_model=list[schemas.Course])
def get_courses_for_user(user_id: int, db: Session = Depends(get_db)):
    # Call the CRUD function to get all courses for a user
    return crud.get_user_courses(db, user_id)

# Remove a course from a user
@app.delete("/users/{user_id}/courses/{course_id}", response_model=schemas.User)
def remove_course_from_user(user_id: int, course_id: int, db: Session = Depends(get_db)):
    # Call the CRUD function to remove a course from a user
    return crud.remove_user_from_course(db, user_id, course_id)
