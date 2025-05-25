
# Project Instructions (I am using a Macbook)

## Basic Setup

### Install Django 

pip3 install django

### Create a new directory

mkdir Wallet
cd Wallet 
pwd

### Create a new Django project

django-admin startproject config_project

### Create a new Django app

python3 manage.py startapp wallet_app

### Open the config_project/settings.py file and add your new app to the INSTALLED_APPS list

![alt text](image.png)

### Run migrations to set up your database

python3 manage.py migrate

![alt text](image-1.png)

### Test your Django installation by running the development server

python3 manage.py runserver

Visit http://127.0.0.1:8000/ in your browser. You should see the Django welcome page.

![alt text](image-2.png)

 git remote add origin https://github.com/francheco/Python.git

###  Open the config_project/models.py and create two models: one for Users and one for Transactions

![alt text](image-3.png)

### Create and apply migrations

python3 manage.py makemigrations

![alt text](image-5.png)

python3 manage.py migrate 

![alt text](image-6.png)

### Run and Test the code

cd Django/Wallet/config_project
python3 mock_data.py

![alt text](image-7.png)

## Open a Python shell in your Django project

cd Django/Wallet/
python manage.py shell

## Test 

### Import modules

from django.contrib.auth.models import User
from wallet_app.models import UserProfile, Transaction

### Check the number of users

print(User.objects.count())  # Should print 10

### Check the number of user profiles

print(UserProfile.objects.count())  # Should print 10

### Check the number of transactions

print(Transaction.objects.count())  # Should print 240 (10 users x 24 transactions)

# You can also check the data for a specific user

user = User.objects.first()
print(user.username)
print(user.userprofile.balance)
print(user.transaction_set.all())

## Crete Django views and templates to display user information

### Create views 

cd Django/Wallet/wallet_app/views.py

![alt text](image-8.png)

### Create templates

cd Django/Wallet/wallet_app/
mkdir templates
cd templates
touch dashboards.html

Create Dashboard

![alt text](image-9.png)

Create Base

touch dashboards.html

![alt text](image-10.png)

#### Update urls.py with the new URL pattern

![alt text](image-11.png)

### Quick test to check everything is working well

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py check

![alt text](image-13.png)

## Create a superuser

### User and password

python3 manage.py createsuperuser

![alt text](image-14.png)

## Running  and testing the app

### running

python3 config_project/mock_data.py
python3 manage.py runserver

![alt text](image-16.png)

### Test the admin interface

http://127.0.0.1:8000/admin/


![alt text](image-17.png)

![alt text](image-18.png)

### Test the Dashboard

http://127.0.0.1:8000/dashboard/

![alt text](image-27.png)

## Adding Transactions

### Create a Form

cd cd Django/Wallet/wallet_app/
touch forms.py

### Update views.py

![alt text](image-19.png)

### Create a Template for the add transaction form

cd cd Django/Wallet/wallet_app/templates
touch add_transaction.html 

![alt text](image-22.png)

### Update urls.py

![alt text](image-23.png)

### Test Add Transaction Form

http://127.0.0.1:8000/add-transaction/

![alt text](image-28.png)


## Viewing Reports

### Update views.py

![alt text](image-24.png)

![alt text](image-29.png)


### Create a template to display the reports

cd cd Django/Wallet/wallet_app/templates
touch reports.html 

![alt text](image-25.png)

### Update urls.py

![alt text](image-26.png)


### Test Viewing Reports

http://127.0.0.1:8000/reports/

![alt text](image-30.png)



























