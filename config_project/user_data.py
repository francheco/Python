
import os
# Import the os module, which provides functions for interacting with the operating system.

import sys
# Import the sys module, which provides access to system-specific parameters and functions.

import django
# Import Django, which is used to interact with the Django framework.

# Get the project's root directory (one level up from the current file)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# - 'os.path.abspath(__file__)' gets the absolute path of the current file (user_data.py).
# - 'os.path.dirname()' gets the directory containing the current file.
# - 'os.path.dirname()' is called twice to get the project's root directory.

sys.path.insert(0, PROJECT_ROOT)
# Add the project's root directory to the Python path.
# This ensures that Python can find modules and packages in the project's root directory.

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wallet_project.settings')
# Set the Django settings module to 'wallet_project.settings'.
# This allows the script to access Django's settings and models.

django.setup()
# Initialize Django. This must be called before importing models or using Django's ORM.

import pandas as pd
# Import the pandas library, which is used for data manipulation and analysis.

from datetime import datetime, timedelta
# Import the datetime and timedelta classes from the datetime module.
# These are used to work with dates and times.

from random import uniform, choice, randint
# Import the uniform, choice, and randint functions from the random module.
# These are used to generate random numbers and select random choices.

from django.contrib.auth.models import User
# Import Django's built-in User model, which represents users in the application.

from wallet_app.models import UserProfile, Transaction
# Import the UserProfile and Transaction models from the wallet_app application.

def user_data():
    # Define a function named user_data. This function generates mock data for the application.

    # Create or update 10 users
    users = [f'user{i}' for i in range(1, 11)]
    # Create a list of usernames (e.g., 'user1', 'user2', ..., 'user10').

    user_data = {'username': users, 'email': [f'{u}@gmail.com' for u in users]}
    # Create a dictionary containing the usernames and corresponding email addresses.

    user_df = pd.DataFrame(user_data)
    # Create a pandas DataFrame from the user data (optional, not used further in the script).

    # Create or update user profiles
    user_profiles = []
    # Initialize an empty list to store UserProfile objects.

    for user in users:
        # Loop through each username.

        user_obj, created = User.objects.get_or_create(username=user, defaults={'email': f"{user}@gmail.com"})
        # Fetch or create a User object for the username.
        # - 'user_obj' is the User object.
        # - 'created' is a boolean indicating whether the User was just created.

        user_profile, profile_created = UserProfile.objects.get_or_create(
            user=user_obj,
            defaults={'balance': uniform(500, 5000)}
        )
        # Fetch or create a UserProfile object for the User.
        # - 'user_profile' is the UserProfile object.
        # - 'profile_created' is a boolean indicating whether the UserProfile was just created.
        # The 'defaults' parameter sets the initial balance to a random value between 500 and 5000.

        if not profile_created:
            # If the UserProfile already exists, update the balance.

            user_profile.balance = uniform(500, 5000)
            # Set the balance to a new random value between 500 and 5000.

            user_profile.save()
            # Save the updated UserProfile to the database.

    # Create transactions
    start_date = datetime(2023, 1, 1)
    # Define the start date for generating transactions.

    end_date = datetime(2024, 12, 31)
    # Define the end date for generating transactions.

    days_range = (end_date - start_date).days
    # Calculate the total number of days between the start and end dates.

    transaction_data = []
    # Initialize an empty list to store Transaction objects.

    for user in users:
        # Loop through each username.

        user_obj = User.objects.get(username=user)
        # Fetch the User object for the username.

        for _ in range(24):
            # Generate 24 transactions for each user.

            random_days = randint(0, days_range)
            # Generate a random number of days between 0 and the total number of days.

            date = start_date + timedelta(days=random_days)
            # Calculate the transaction date by adding the random number of days to the start date.

            amount = uniform(10, 500)
            # Generate a random transaction amount between 10 and 500.

            category = choice(['FOOD', 'TRANSPORT', 'ENTERTAINMENT', 'SHOPPING', 'BILLS', 'OTHER'])
            # Select a random transaction category from the predefined choices.

            description = f'Sample transaction for {user}'
            # Create a description for the transaction.

            transaction = Transaction(
                user=user_obj,
                amount=amount,
                category=category,
                date=date,
                description=description
            )
            # Create a Transaction object with the generated data.

            transaction_data.append(transaction)
            # Add the Transaction object to the list.

    Transaction.objects.bulk_create(transaction_data)
    # Save all the Transaction objects to the database in a single query.

    print('Mock data generated successfully!')
    # Print a success message to the console.

if __name__ == '__main__':
    # Check if the script is being run directly (not imported as a module).

    user_data()
    # Call the user_data function to generate mock data.