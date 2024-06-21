from django.shortcuts import render

def home_page(request):
    return render(request,'home.html')

def home_page2(request):
    return render(request,'home2.html')