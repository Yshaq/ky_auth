from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'frontend/login.html')

def profile_view(request):
    return render(request, 'frontend/profile.html')

def register_view(request):
    return render(request, 'frontend/register.html')

def landing_view(request):
    return render(request, 'frontend/landing.html')