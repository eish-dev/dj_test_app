"""
URL configuration for dj_test_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.urls import re_path as url

from lms_app import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

app_name = "test"



urlpatterns = [
    path('checkout/', views.checkout_book, name='checkout_book'),
    path('return/', views.return_book, name='return_book'),
    path('overdue/', views.get_overdues, name='overdues'),
    path('fulfil/', views.get_overdues, name='fulfil'),
    path('handle/', views.handle_event, name='handle_event')
]