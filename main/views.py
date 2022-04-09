from django.shortcuts import render
from . models import Author,About, Fact, Skill, Testimonials

def home(request):
    authors = Author.objects.all()
    context = {
        'authors':authors,
    }
    return render(request,'index.html',context)
    

def about(request):
    abouts = About.objects.all()
    skills = Skill.objects.all()
    facts = Fact.objects.all()
    testimonials = Testimonials.objects.all()
    # print(about)
    context = {
        'abouts':abouts,
        'skills':skills,
        'facts':facts,
        'testimonials':testimonials
    }
    return render(request,'about.html',context)

def contact(request):
    return render(request,'contact.html')

def portfolio(request):
    return render(request,'portfolio.html')

def resume(request):
    return render(request,'resume.html')

def services(request):
    return render(request,'services.html')
