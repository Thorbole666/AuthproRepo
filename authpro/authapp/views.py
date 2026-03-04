from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')

@login_required
def java_exam_view(request):
    return render(request,'testapp/java_exam.html')

@login_required
def apti_exam_view(request):
    return render(request,'testapp/apti_exam.html')

@login_required
def django_exam_view(request):
    return render(request,'testapp/django_exam.html')

def logout_view(request):
    return render(request,'testapp/logout.html')

def register_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        User.objects.create_user(username=username,password=password)#convert our password to hash format.
        return redirect('/')
    return render(request,'testapp/register.html')
