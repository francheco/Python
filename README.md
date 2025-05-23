# Python



# Instructions (I am using a MacBook)

## Set up your Django project

###  install Django

pip3 install django

### Create a new directory 

cd /Your/Path/Folder/Name/

mkdir Django
cd Django

### Create a new Django project

django-admin startproject wallet_project

### Create a new Django app

cd wallet_project
python3 manage.py startapp wallet_app

### Open the project wallet_project/settings.py file and add your new app to the INSTALLED_APPS list

INSTALLED_APPS = [

'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wallet_app',  # Add this line
]

<img width="868" alt="image" src="https://github.com/user-attachments/assets/c87f1eb8-9928-4fb9-8d80-97643bc8bac5" />


### Run migrations to set up the database

python3 manage.py migrate

<img width="576" alt="image" src="https://github.com/user-attachments/assets/205a0e23-f466-4dc6-8777-570f36d4030d" />


### Test the Django installation by running the development server

python3 manage.py runserver

Go to  http://127.0.0.1:8000/ in your browser. You should see the Django welcome page.

<img width="868" alt="image" src="https://github.com/user-attachments/assets/765c407b-212f-4360-9f61-0f0552b20e32" />


<img width="1193" alt="image" src="https://github.com/user-attachments/assets/cf655c27-7f3d-4b8b-96bd-9eb996c7184a" />



########################################################################################################

#  Setting up Django models

This will be the foundation for storing user and transaction data.

## Models

Django models form the backbone of the application's data layer. They define how the data is structured, stored, and retrieved, which is crucial for building a functional web application to analyse spending patterns.

Let's break down why we need Django models and what they do.

Database Abstraction: allows for the definition of data structures in Python code without having to write SQL directly.

Data Structure Definition: specify what fields (like name, email, amount, date, etc.) each type of data should have.

Data Validation: Specify that a field must be unique or can't be blank.

Object-Relational Mapping (ORM): allows interaction with the database using Python code instead of SQL.

Admin Interface Integration: automatically generates an admin interface based on the models, which can be very useful for managing the data

Query Facilitation: Provides a powerful and intuitive way to query your database. You can easily filter, order, and aggregate data.

# Code Considerations

Open the models.py file in the wallet_app directory and create two models: Users and Transactions.

UserProfile: This extends the built-in Django User model to include a balance field.

Transaction: This model represents individual transactions, including fields for amount, category, date, and description.

These models will allow you to:

Store user information and their associated transactions
Query the database to analyse spending patterns
Integrate with Django's built-in authentication system
Provide a structure for your mock data and future real data

After adding these models, you need to create and apply migrations.

#### Create migrations

python3 manage.py makemigrations

<img width="595" alt="image" src="https://github.com/user-attachments/assets/5e6a79d7-713e-4307-ae72-f9103f96842d" />


### Apply migrations

python3 manage.py migrate

<img width="532" alt="image" src="https://github.com/user-attachments/assets/81dcbf24-cdb0-4206-b000-ecc8573a3ceb" />


########################################################################################################

# Generate Mock User Data

I have created the user_data.py file in the wallet_project root directory. 

### Run the script

python3 user_data.py

After running the script, you should see the output: Mock data generated successfully! 

Or whatever you put on the print

### Test the script

Open a Python shell in the Django/wallet_project project directory.

python3 manage.py shell

from django.contrib.auth.models import User
from wallet_app.models import UserProfile, Transaction

### Check the number of users

print(User.objects.count())  # Should print 10

### Check the number of user profiles

print(UserProfile.objects.count())  # Should print 10

### Check the number of transactions

print(Transaction.objects.count())  # Should print 240 (10 users x 24 transactions)

### You can also check the data for a specific user
user = User.objects.first()
print(user.username)
print(user.userprofile.balance)
print(user.transaction_set.all())

########################################################################################################

# Created Django views and templates

## Create Views

Update the views.py file on the wallet_app path with the script. 

## Create Templates

### Create the new folder

mkdir -p wallet_app/templates/wallet_app

### Create the new  HTML file

cd wallet_app/templates/wallet_app/

touch dashboard.html

Update the dashboard.html file with the script 

### Set up URL patterns

Update the urls.py file on the wallet_app path with the script 

### Create the new  HTML file

cd  wallet_app/templates/wallet_app/

touch base.html

Update the base.html file with the script 

########################################################################################################

# Tested Django views and templates


### Make sure the database is up to date

python3 manage.py makemigrations
python3 manage.py migrate

### Create a superuser

python3 manage.py createsuperuser

Creates an admin account to access the Django admin interface.

Follow the prompts to enter a username, email, and password. Once created, you can log in to the admin panel.


<img width="610" alt="image" src="https://github.com/user-attachments/assets/d3f03f9b-8f10-41a0-9937-abd486b0cfdd" />


### Run user_data.py script to populate the database with mock data

python3 wallet_project/user_data.py

### Start the Django development server

python3 manage.py runserver

<img width="1201" alt="image" src="https://github.com/user-attachments/assets/f7dc244f-0d43-4254-abe0-b0f0a0898901" />

### Test the Admin Interface

Open a web browser and navigate to http://127.0.0.1:8000/admin/

<img width="661" alt="image" src="https://github.com/user-attachments/assets/16c8b77a-fe8a-4b92-b85d-6b63c4f34e3e" />


Log in with your superuser credentials.
Here, you should be able to see and manage your User, UserProfile, and Transaction models.

<img width="1252" alt="image" src="https://github.com/user-attachments/assets/32e6f7e1-1c48-4688-9a1b-198f948987cd" />

<img width="1265" alt="image" src="https://github.com/user-attachments/assets/1690eb9f-db84-480d-8ac0-991c683977d4" />

<img width="1268" alt="image" src="https://github.com/user-attachments/assets/bd6bda41-b538-414b-8c6e-119583bcf7f9" />

### Test the Dashboard

Navigate to your dashboard URL http://127.0.0.1:8000/dashboard/

<img width="860" alt="image" src="https://github.com/user-attachments/assets/ec78fa1c-abbd-4852-a684-3025b73f7a7b" />


You should see your dashboard page with user information and transactions.

If your dashboard view is working correctly, you should see:

User balance

Recent transactions

Any other information you've included in your dashboard template.

At this point our project work well, let's add more functionalities. 

########################################################################################################

# Adding Transactions

### Create a Form

Create a forms.py file in the wallet_app directory.
Define a TransactionForm for adding transactions.

### Update views.py

Add a view to handle the form submission.

### Create a Template

Create a template for the add transaction form.

### Update urls.py

Add a URL pattern for the add transaction view.

########################################################################################################

# Filtering Transactions

### Update views.py

Modify the dashboard view to handle filtering.

### Update dashboard.html

Add a filter dropdown to the template.

########################################################################################################

# Viewing Reports

### Update views.py

Add a view to generate reports.

### Create a Template

Create a template to display the reports.

### Update urls.py

Add a URL pattern for the reports view.

########################################################################################################

# Test Additional Functionality

### Adding Transactions

Add a transaction 

http://127.0.0.1:8000/add-transaction/

<img width="815" alt="image" src="https://github.com/user-attachments/assets/043d981b-56c1-4037-8af6-5d4df2bcba25" />


### Filtering Transactions

Filter transactions on the dashboard

http://127.0.0.1:8000/dashboard/

<img width="804" alt="image" src="https://github.com/user-attachments/assets/4c0d051e-a53a-46b0-8bfd-ed12e6474b29" />


### Viewing Reports

View reports

http://127.0.0.1:8000/reports/

<img width="1223" alt="image" src="https://github.com/user-attachments/assets/4b60d737-64aa-444e-865d-4d438390a32c" />

########################################################################################################

# How to Clear Mock Data

If you want to start fresh and remove the mock data, you can delete all transactions and users from the database.

### Using the Django Shell

python3 manage.py shell

from django.contrib.auth.models import User
from wallet_app.models import Transaction, UserProfile

### Delete all transactions

Transaction.objects.all().delete()

### Delete all user profiles

UserProfile.objects.all().delete()

### Delete all users (except the superuser)

User.objects.filter(is_superuser=False).delete()
















 
