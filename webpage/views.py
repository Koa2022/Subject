from django.shortcuts import render

# Create your views here.

from . import models

def home(request):
    context = {}
    
    subject = models.Subject.objects.all().order_by('name')
    context['subjects'] = subject
    
    return render(request, 'home.html', context)

def category1(request):
    context = {}
    
    subject = models.Subject.objects.filter(category=1).order_by('name')
    context['subjects'] = subject
    
    return render(request, 'page1.html', context)

def category2(request):
    context = {}
    
    subject = models.Subject.objects.filter(category=2).order_by('name')
    context['subjects'] = subject
    
    return render(request, 'page2.html', context)

def category3(request):
    context = {}
    
    subject = models.Subject.objects.filter(category=3).order_by('name')
    context['subjects'] = subject
    
    return render(request, 'page3.html', context)