from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('<int:quiz_id>/', views.home, name='home_page'),
    path('email/', views.send_email, name='send_email'),
]
