"""
URL configuration for config_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
# Import Django's admin module, which provides the admin interface.

from django.urls import path
# Import Django's path function, which is used to define URL patterns.

from wallet_app import views
# Import the views from the wallet_app application.

import os
# Import the os module, which provides functions for interacting with the operating system.

import sys
# Import the sys module, which provides access to system-specific parameters and functions.

# Get the project's root directory (one level up from the current file)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# - 'os.path.abspath(__file__)' gets the absolute path of the current file (urls.py).
# - 'os.path.dirname()' gets the directory containing the current file.
# - 'os.path.dirname()' is called twice to get the project's root directory.

sys.path.insert(0, PROJECT_ROOT)
# Add the project's root directory to the Python path.
# This ensures that Python can find modules and packages in the project's root directory.

urlpatterns = [
    # Define a list of URL patterns for the project.

    path('admin/', admin.site.urls),
    # Map the 'admin/' URL to Django's admin interface.

    path('dashboard/', views.dashboard, name='dashboard'),
    # Map the 'dashboard/' URL to the dashboard view in the wallet_app application.
    # The 'name' parameter allows you to refer to this URL pattern in templates and views.

    path('add-transaction/', views.add_transaction, name='add_transaction'),
    # Map the 'add-transaction/' URL to the add_transaction view in the wallet_app application.
    # The 'name' parameter allows you to refer to this URL pattern in templates and views.

    path('reports/', views.reports, name='reports'),
    # Map the 'reports/' URL to the reports view in the wallet_app application.
    # The 'name' parameter allows you to refer to this URL pattern in templates and views.
]