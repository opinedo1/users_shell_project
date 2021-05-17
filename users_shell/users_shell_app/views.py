from django.shortcuts import render, redirect, HttpResponse
from .models import User

# Create your views here.
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'index.html', context)

def add_user(request):
    print(request.POST)
    return redirect('/')