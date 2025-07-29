from django.shortcuts import render
from django.views.generic import TemplateView


def admin_hai(request):
    return render(request, 'Admin/hai.html')

def admin_template(request):
    return render(request, 'Admin/AdminTemplates/Dashboard.html')