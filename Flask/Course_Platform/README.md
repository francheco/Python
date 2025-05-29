
# Instructions (I am using a macbook)

## Set up the development environment

### Set up a virtual environment

mkdir Course_Platform
cd Course_Platform
python3 -m venv venv
source venv/bin/activate

### Install required packages

pip3 install Flask mysql-connector-python
pip3 install mysql-connector-python
pip3 list

### Create a requirements.txt file

Flask
mysql-connector-python

## Testing the environment

## Creating & Running a test file. 

Created the app.py file in your project directory to return  return "Hello, Course Portfolio!"

![alt text](image.png)

Running the file 

python3 app.py

![alt text](image-2.png)

Running on http://127.0.0.1:5000

![alt text](image-1.png)

## Set up MysQL Database

### MySQL Workbench

I created a new scheme named course_portfolio

### Design the Database Schema

create two tables in your database: one for courses and one for users.

![alt text](image-3.png)

![alt text](image-4.png)

### Connecting the app to the Database

update the app.py file to connect to the MySQL database.

![alt text](image-5.png)

If the database connection is successful, you’ll see a message like

![alt text](image-6.png)

## Create API Endpoints for CRUD Operations

### Create Flask routes to handle CRUD operations

Update your app.py file

![alt text](image-7.png)

### Test the app

python3 app.py

http://127.0.0.1:5000/. You should see the message

![alt text](image-8.png)

## Test API Endpoints

### Add a New Course (POST)

Use a tool like Postman

URL: http://127.0.0.1:5000/courses
Method: POST
Body (raw): 

![alt text](image-9.png)

Response:

![alt text](image-10.png)

### Get All Courses (GET)

URL: http://127.0.0.1:5000/courses
Method: GET

Response:

![alt text](image-11.png)

![alt text](image-12.png)

### Update a Course (PUT)

URL: http://127.0.0.1:5000/courses/4  (I choose the course_id 4)
Method: PUT
Body (raw):

![alt text](image-13.png)

Response:

![alt text](image-14.png)

![alt text](image-15.png)

### Delete a Course (DELETE)

URL: http://127.0.0.1:5000/courses/4
Method: DELETE

Response:

![alt text](image-16.png)

![alt text](image-17.png)

![alt text](image-18.png)




























