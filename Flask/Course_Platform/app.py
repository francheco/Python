

# Import the Flask class, jsonify function, and request object from the Flask library
from flask import Flask, jsonify, request

# Import the MySQL connector library to interact with the MySQL database
import mysql.connector

# Create an instance of the Flask class. This is the core of the web application.
app = Flask(__name__)

# Define the database configuration as a dictionary
db_config = {
    'host': 'localhost',  # The host where the MySQL database is running
    'user': 'root',       # The MySQL username (replace with your username)
    'password': 'franklin',  # The MySQL password (replace with your password)
    'database': 'course_portfolio'  # The name of the database to connect to
}

# Define a helper function to establish a connection to the MySQL database
def get_db_connection():
    # Use the mysql.connector.connect() method to create a connection using the db_config dictionary
    conn = mysql.connector.connect(**db_config)
    # Return the connection object so it can be used in other functions
    return conn

# Define a route for the root URL ("/")
@app.route('/')
def index():
    # Return a simple welcome message when the root URL is accessed
    return "Welcome to the Course Portfolio API!"

# Define a route for the "/courses" URL that only accepts GET requests
@app.route('/courses', methods=['GET'])
def get_courses():
    try:
        # Establish a connection to the database
        conn = get_db_connection()
        # Create a cursor object that returns results as dictionaries
        cursor = conn.cursor(dictionary=True)
        # Execute a SQL query to select all rows from the "courses" table
        cursor.execute("SELECT * FROM courses")
        # Fetch all rows from the query result
        courses = cursor.fetchall()
        # Close the cursor to free up resources
        cursor.close()
        # Close the database connection
        conn.close()
        # Return the fetched courses as a JSON response
        return jsonify(courses)
    except Exception as e:
        # If an error occurs, return an error message with a 500 status code
        return jsonify({"error": str(e)}), 500

# Define a route for the "/courses" URL that only accepts POST requests
@app.route('/courses', methods=['POST'])
def add_course():
    try:
        # Retrieve the JSON data sent in the request body
        data = request.get_json()
        # Establish a connection to the database
        conn = get_db_connection()
        # Create a cursor object
        cursor = conn.cursor()
        # Execute a SQL query to insert a new course into the "courses" table
        cursor.execute(
            "INSERT INTO courses (subject, title, description) VALUES (%s, %s, %s)",
            (data['subject'], data['title'], data['description'])
        )
        # Commit the transaction to save the changes to the database
        conn.commit()
        # Close the cursor
        cursor.close()
        # Close the database connection
        conn.close()
        # Return a success message with a 201 status code (Created)
        return jsonify({"message": "Course added successfully!"}), 201
    except Exception as e:
        # If an error occurs, return an error message with a 500 status code
        return jsonify({"error": str(e)}), 500

# Define a route for the "/courses/<course_id>" URL that only accepts PUT requests
@app.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    try:
        # Retrieve the JSON data sent in the request body
        data = request.get_json()
        # Establish a connection to the database
        conn = get_db_connection()
        # Create a cursor object
        cursor = conn.cursor()
        # Execute a SQL query to update the course with the specified course_id
        cursor.execute(
            "UPDATE courses SET subject = %s, title = %s, description = %s WHERE course_id = %s",
            (data['subject'], data['title'], data['description'], course_id)
        )
        # Commit the transaction to save the changes to the database
        conn.commit()
        # Close the cursor
        cursor.close()
        # Close the database connection
        conn.close()
        # Return a success message
        return jsonify({"message": "Course updated successfully!"})
    except Exception as e:
        # If an error occurs, return an error message with a 500 status code
        return jsonify({"error": str(e)}), 500

# Define a route for the "/courses/<course_id>" URL that only accepts DELETE requests
@app.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    try:
        # Establish a connection to the database
        conn = get_db_connection()
        # Create a cursor object
        cursor = conn.cursor()
        # Execute a SQL query to delete the course with the specified course_id
        cursor.execute("DELETE FROM courses WHERE course_id = %s", (course_id,))
        # Commit the transaction to save the changes to the database
        conn.commit()
        # Close the cursor
        cursor.close()
        # Close the database connection
        conn.close()
        # Return a success message
        return jsonify({"message": "Course deleted successfully!"})
    except Exception as e:
        # If an error occurs, return an error message with a 500 status code
        return jsonify({"error": str(e)}), 500

# Ensure the Flask app only runs if the script is executed directly (not imported as a module)
if __name__ == '__main__':
    # Start the Flask development server with debugging enabled
    app.run(debug=True)

