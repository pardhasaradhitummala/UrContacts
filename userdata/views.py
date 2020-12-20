from django.shortcuts import render



def home_screen(request):
    return render(request,'registration/home_screen.html')

def login_screen(request):
    return render(request,'registration/login_screen.html')
