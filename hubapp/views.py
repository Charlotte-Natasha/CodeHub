from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login")
def index(request):

    return render(request, 'hubapp/index.html')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        image = request.FILES.get('image')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        profile = Profile.objects.create(user=user, profile_picture=image)
        user.save()
        profile.save()

        if profile:
            return redirect('login')
    else:  
        return render(request, 'registration/signup.html', {})     

def contact(request):

    return render(request, 'hubapp/contact.html')    

def resources(request):

    return render(request, 'hubapp/resources.html') 

def community(request):
    post = Post.objects.all()
    comment = Comment.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('community')
    else:
        form = PostForm()

    return render(request, 'hubapp/community.html', {'comment':comment, 'post':post}) 

def process(request):

    return render(request, 'hubapp/process.html')

def profile(request):
    user = request.user
    profile = Profile.objects.get( user = user)

    return render(request, 'hubapp/profile.html', {'profile':profile, 'user':user})  

def details(request, id):
    post = Post.objects.filter(id=id).first()
    comment = Comment.objects.filter(post=post).order_by('date')
    user = request.user

    if request.method == 'POST':    
        form = CommentForm()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = user 
            comment.save()
    else:
        form = CommentForm()        
    return render(request, 'hubapp/details.html', {'post':post, 'form':form, 'comment':comment})          

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

