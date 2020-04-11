from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from homepage.forms import ReportForm
from .models import Report

def home(request):
    all_reports = Report.objects.all()
    return render(request, 'homepage/home.html', {'Reports':all_reports})

def about(request):
    return render(request, 'homepage/about.html')

def report_create_view(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.author = request.user
            report.save()
            return redirect('homepage')
    else:
        form = ReportForm()

    return render(request, 'homepage/report.html', {"form":form})