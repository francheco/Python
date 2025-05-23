

# Create your views here.

from django.shortcuts import render, redirect
# Import Django's render and redirect functions.
# - 'render' is used to render templates.
# - 'redirect' is used to redirect the user to another URL.

from django.contrib.auth.decorators import login_required
# Import the login_required decorator, which ensures that only logged-in users can access the view.

from .models import UserProfile, Transaction
# Import the UserProfile and Transaction models from the current app (wallet_app).

from .forms import TransactionForm
# Import the TransactionForm from the current app (wallet_app).

from django.db.models import Sum
# Import the Sum aggregation function, which is used to calculate totals in the reports view.

@login_required
def dashboard(request):
    # Define a view named dashboard. This view displays the user's dashboard.
    # The @login_required decorator ensures that only logged-in users can access this view.

    # Use get_or_create to ensure a UserProfile exists for the user
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    # Fetch the UserProfile for the logged-in user. If it doesn't exist, create it.
    # - 'user_profile' is the UserProfile object.
    # - 'created' is a boolean indicating whether the UserProfile was just created.

    # Fetch transactions with optional filtering by category
    category = request.GET.get('category')
    # Get the selected category from the URL query parameters (e.g., ?category=FOOD).

    transactions = Transaction.objects.filter(user=request.user)
    # Fetch all transactions for the logged-in user.

    if category:
        transactions = transactions.filter(category=category)
        # If a category is selected, filter transactions by that category.

    # Fetch recent transactions (limit to 20)
    recent_transactions = transactions.order_by('-date')[:20]
    # Fetch the most recent 20 transactions, ordered by date (newest first).

    # Prepare context for the template
    context = {
        'user_profile': user_profile,
        'recent_transactions': recent_transactions,
    }
    # Create a dictionary containing the data to pass to the template.

    return render(request, 'wallet_app/dashboard.html', context)
    # Render the 'dashboard.html' template with the provided context.

@login_required
def add_transaction(request):
    # Define a view named add_transaction. This view handles adding new transactions.
    # The @login_required decorator ensures that only logged-in users can access this view.

    if request.method == 'POST':
        # Check if the form was submitted (POST request).

        form = TransactionForm(request.POST)
        # Create a TransactionForm instance with the submitted data.

        if form.is_valid():
            # Check if the form data is valid.

            transaction = form.save(commit=False)
            # Save the form data to a Transaction object but don't commit it to the database yet.

            transaction.user = request.user
            # Set the user of the transaction to the logged-in user.

            transaction.save()
            # Save the transaction to the database.

            return redirect('dashboard')
            # Redirect the user to the dashboard after saving the transaction.

    else:
        # If the form was not submitted (GET request), create an empty form.

        form = TransactionForm()
        # Create an empty TransactionForm instance.

    return render(request, 'wallet_app/add_transaction.html', {'form': form})
    # Render the 'add_transaction.html' template with the form.

@login_required
def reports(request):
    # Define a view named reports. This view displays spending reports.
    # The @login_required decorator ensures that only logged-in users can access this view.

    transactions = Transaction.objects.filter(user=request.user)
    # Fetch all transactions for the logged-in user.

    monthly_spending = transactions.values('date__month').annotate(total=Sum('amount'))
    # Calculate the total spending for each month.
    # - 'values('date__month')' groups transactions by month.
    # - 'annotate(total=Sum('amount'))' calculates the total spending for each group.

    category_spending = transactions.values('category').annotate(total=Sum('amount'))
    # Calculate the total spending for each category.
    # - 'values('category')' groups transactions by category.
    # - 'annotate(total=Sum('amount'))' calculates the total spending for each group.

    context = {
        'monthly_spending': monthly_spending,
        'category_spending': category_spending,
    }
    # Create a dictionary containing the data to pass to the template.

    return render(request, 'wallet_app/reports.html', context)
    # Render the 'reports.html' template with the provided context.