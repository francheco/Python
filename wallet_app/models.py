

# Create your models here.

from django.db import models
# Import Django's models module, which provides tools for defining database models.

from django.contrib.auth.models import User
# Import Django's built-in User model, which represents users in the application.

class UserProfile(models.Model):
    # Define a model named UserProfile. 
    # This model extends the built-in User model to include additional fields.

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Create a one-to-one relationship with the User model.
    # The 'on_delete=models.CASCADE' ensures that if a User is deleted, their UserProfile is also deleted.

    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # Create a DecimalField named 'balance' to store the user's balance.
    # 'max_digits=10' allows up to 10 digits in total.
    # 'decimal_places=2' allows up to 2 decimal places.
    # 'default=0' sets the default balance to 0.

    def __str__(self):
        # Define a string representation for the UserProfile model.
        # This is used to display the UserProfile in the Django admin and other places.
        return self.user.username
        # Return the username of the associated User.

class Transaction(models.Model):
    # Define a model named Transaction. 
    # This model represents a financial transaction in the application.

    CATEGORY_CHOICES = [
        # Define a list of choices for the 'category' field.
        # Each choice is a tuple of (value, label).
        ('FOOD', 'Food'),
        ('TRANSPORT', 'Transport'),
        ('ENTERTAINMENT', 'Entertainment'),
        ('SHOPPING', 'Shopping'),
        ('BILLS', 'Bills'),
        ('OTHER', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Create a foreign key relationship with the User model.
    # The 'on_delete=models.CASCADE' ensures that if a User is deleted, their transactions are also deleted.

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Create a DecimalField named 'amount' to store the transaction amount.
    # 'max_digits=10' allows up to 10 digits in total.
    # 'decimal_places=2' allows up to 2 decimal places.

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    # Create a CharField named 'category' to store the transaction category.
    # 'max_length=20' limits the length of the category name to 20 characters.
    # 'choices=CATEGORY_CHOICES' restricts the category to the predefined choices.

    date = models.DateTimeField(auto_now_add=True)
    # Create a DateTimeField named 'date' to store the transaction date.
    # 'auto_now_add=True' automatically sets the date to the current date and time when the transaction is created.

    description = models.TextField(blank=True)
    # Create a TextField named 'description' to store additional details about the transaction.
    # 'blank=True' allows the field to be optional (i.e., it can be left empty).

    def __str__(self):
        # Define a string representation for the Transaction model.
        # This is used to display the Transaction in the Django admin and other places.
        return f"{self.user.username} - {self.amount} - {self.category}"
        # Return a string in the format "username - amount - category".