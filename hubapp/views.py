from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'hubapp/index.html')

def contact(request):

    return render(request, 'hubapp/contact.html')    

def resources(request):

    return render(request, 'hubapp/resources.html') 

def community(request):

    return render(request, 'hubapp/community.html') 
