
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

### Open the wallet_project/settings.py file and add your new app to the INSTALLED_APPS list

![alt text](image.png)

### Run migrations to set up your database

python3 manage.py migrate

![alt text](image-1.png)

### Test your Django installation by running the development server

python3 manage.py runserver

Visit http://127.0.0.1:8000/ in your browser. You should see the Django welcome page.

![alt text](image-2.png)

 git remote add origin https://github.com/francheco/Python.git

 




