from django.shortcuts import render, redirect, HttpResponse
from .models import User

# Reads the data from our database and puts it in context
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'index.html', context)


# Adds new users to our database that is received from our POST request
def add_user(request):
    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email_address = request.POST['email_address'],
        age = request.POST['age']
    )
    return redirect('/')