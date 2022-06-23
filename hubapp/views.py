from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.template import loader
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

def profile(request):

    return render(request, 'hubapp/profile.html')    

def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    profile = Profile.objects.get(user=user)

    fuser = post.user
    fprofile = Profile.objects.get(user=fuser)

    #Profile info box
    posts_count = Post.objects.filter(user=fuser).count()

    comments = Comment.objects.filter(post=post).order_by('date')
    
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = user
            comment.save()
            return HttpResponseRedirect(reverse('post', args=[post_id]))
    else:
        form = CommentForm()
        template = loader.get_template('post.html')

    context = {
    'post':post,
    'profile':profile,
    'form':form,
    'comments':comments,
    }

    return HttpResponse(template.render(context, request))             

