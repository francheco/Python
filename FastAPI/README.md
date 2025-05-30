
# Instructions (I am using a macbook)

## Set up the development environment

### Set up a virtual environment

mkdir Course_Platform
cd Course_Platform
python3 -m venv venv
source venv/bin/activate

### Install required packages

pip3 install fastapi uvicorn sqlalchemy pymysql

### Create the Project Structure

Course_Platform/
main.py
models.py
schemas.py
crud.py
database.py
requirements.txt

### Add Dependencies to requirements.txt

pip3 freeze > requirements.txt

### Verify the Setup

pip3 list

![alt text](image.png)

## Test the FastAPI Setup

### Basic configuration

Open main.py and add a basic FastAPI app to test

![alt text](image-1.png)

## Run the FastAPI server

uvicorn main:app --reload

Go to http://127.0.0.1:8000/  You should see the message

![alt text](image-2.png)

## Database Setup

### Connection to the Databse

I am using MySQL workbench, I Created a new database a tested the connectivity

![alt text](image-3.png)

### Tables

courses

![alt text](image-4.png)

users

![alt text](image-6.png)

user_courses entity relationship

![alt text](image-7.png)

## Set Up Database Connection in FastAPI

### Basic Connfiguration

Open database.py and add the script

![alt text](image-12.png)

### Test the connection

Open main.py and add the script

![alt text](image-11.png)

## Run the FastAPI server

uvicorn main:app --reload

go to http://127.0.0.1:8000/test-db.  You should see the message

![alt text](image-13.png)

## FastAPI Models and Schemas

### Define SQLAlchemy Models

Open models.py and define the models

![alt text](image-14.png)

### Define Pydantic Schemas

Open schemas.py and define the schemas for data validation.

![alt text](image-15.png)

### Update database.py to Create Tables

Ensure database.py includes the code to create the tables automatically when the application starts.

![alt text](image-16.png)

### Call create_tables() in main.py

Add the create_tables() function to main.py to ensure the tables are created when the application starts.

![alt text](image-17.png)

then, Verify the tables are created in MySQL Workbench.

## CRUD Operations

### CRUD Functions for Courses

Open crud.py and define the CRUD functions for the courses table.

### CRUD Functions for Users

Add the CRUD functions for the users table in crud.py.

### CRUD Functions for User-Courses Relationship

Add the functions to link users to courses in crud.py

### Update main.py to Add CRUD Endpoints

Open main.py and add the FastAPI endpoints to expose the CRUD operations.

## Run the FastAPI server

uvicorn main:app --reload

go to http://127.0.0.1:8000/docs.  You should see the Swagger UI with all the CRUD endpoints listed

![alt text](image-18.png)

![alt text](image-19.png)

![alt text](image-20.png)

## Test the Endpoints

### Create a course and a user

![alt text](image-21.png)

![alt text](image-22.png)

![alt text](image-23.png)

![alt text](image-24.png)

### Add a course to a user.

Please do it by yourself 

### Retrieve all courses for a user.

Please do it by yourself 

### Update and delete records.

Please do it by yourself 






