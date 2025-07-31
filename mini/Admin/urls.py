from django.urls import path
from . import views

urlpatterns = [
    path('UserRegistration/', views.register_user, name='admin_hai'),
    path('DisplayUser/', views.display_user, name='display_user'),]
