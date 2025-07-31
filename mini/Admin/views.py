from django.shortcuts import render, redirect
from .models import tbl_user


def register_user(request):
    success = False
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        tbl_user.objects.create(user_name=user_name, password=password)
        success = True
    return render(request, 'Admin/UserRegistration.html', {'success': success})


def display_user(request):
    users = tbl_user.objects.all()
    return render(request, 'Admin/DisplayUser.html', {'users': users})


