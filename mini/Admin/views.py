from django.shortcuts import render
from django.views.generic import TemplateView

def dashboard(request):
    return render(request, 'Admin/Dashboard.html')

def admin_template(request):
    return render(request, "Admin/AdminTemplates/Dashboard.html")
