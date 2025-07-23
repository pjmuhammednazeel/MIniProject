from django.shortcuts import render

def dashboard(request):
    return render(request, 'Admin/Dashboard.html')
