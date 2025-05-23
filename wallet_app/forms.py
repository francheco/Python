

from django import forms
# Import Django's forms module, which provides tools for creating and handling forms.

from .models import Transaction
# Import the Transaction model from the current app (wallet_app). 
# The form will be based on this model.

class TransactionForm(forms.ModelForm):
    # Define a form class named TransactionForm. 
    # It inherits from Django's ModelForm, which automatically generates form fields based on a model.

    class Meta:
        # Define a nested Meta class to provide metadata for the form. 
        # It tells Django which model to use and which fields to include in the form.

        model = Transaction
        # Specify that the form is based on the Transaction model.

        fields = ['amount', 'category', 'description']
        # Specify the fields from the Transaction model that should be included in the form. 
        # In this case, the form will include fields for 'amount', 'category', and 'description'.