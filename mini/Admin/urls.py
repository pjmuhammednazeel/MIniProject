from django.urls import path
from . import views

urlpatterns = [
    path('AdminTemplate/', views.admin_template, name='admin_template'),
    path('hai/', views.admin_hai, name='admin_hai'),  # new URL
]
