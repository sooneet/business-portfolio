from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def portfolio(request):
    return render(request,'portfolio.html')

def resume(request):
    return render(request,'resume.html')

def services(request):
    return render(request,'services.html')
