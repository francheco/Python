

# Register your models here.

# Import Django's admin module which provides the admin site functionality
from django.contrib import admin

# Import the models that we want to register with the admin site
from .models import UserProfile, Transaction

# Register the UserProfile model with the admin site
admin.site.register(UserProfile)

# Register the Transaction model with the admin site
admin.site.register(Transaction)
