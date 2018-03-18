from django.shortcuts import render

# Create your views here.


def mainpage(request):
    return render(request, 'base.html')

def dashboard(request):
    return render(request, 'dashboard.html')