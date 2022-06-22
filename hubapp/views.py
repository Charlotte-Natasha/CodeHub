from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
def index(request):

    return render(request, 'hubapp/index.html')

def sign_up(request):
    if request.method == 'POST':
    
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # password1 = request.POST['password1']
        image = request.FILES['image']
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        if user:
            messages.success(request,'Profile Created Please Login')
            return redirect('login')
    else:  
        return render(request, 'registration/signup.html', {})     

def contact(request):

    return render(request, 'hubapp/contact.html')    

def resources(request):

    return render(request, 'hubapp/resources.html') 

def community(request):

    return render(request, 'hubapp/community.html') 

def process(request):

    return render(request, 'hubapp/process.html')

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.description = request.user
            post.save()   
            return redirect('community')
    else:
        form = PostForm() 

    return render(request, 'hubapp/post.html', {'form':form})

def profile(request):

    return render(request, 'hubapp/profile.html')              
