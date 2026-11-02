from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login ,logout,authenticate
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Training,Enrollment

# Create your views here.

def home(request):
    return render(request, 'Base.html') 

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)

        user =authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
    return render(request, 'login.html')

def admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)

        user =authenticate(username=username,password=password)
        print(user)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'User not a staff')
                return redirect('admin')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('admin')
    return render(request, 'admin.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cnfpassword = request.POST['confirmPassword']
        if password != cnfpassword:
            messages.error("Please Check the Password")
        else:
            if User.objects.filter(username = username).exists():
                messages.error(request,'Username already exist')
            else:
                user = User.objects.create_user(first_name = name,username=username,password=password,
                                         email=email,)
                user.save()
                return redirect('login')
        return redirect('register')
    return render(request, 'register.html')


def logout_user(request):
    logout (request)
    return redirect('home')



def training_list(request):
    trainings = Training.objects.all()
    return render(request, 'training_list.html', {'trainings': trainings})


def add_training(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        trainer_name = request.POST['trainer_name']
        date = request.POST['date']  # Expect the date in 'YYYY-MM-DDTHH:MM' format
        duration = request.POST['duration']
        price = request.POST['price']

        training = Training(
            title=title,
            description=description,
            trainer_name=trainer_name,
            date=date,
            duration=duration,
            price=price
        )
        training.save()
        return redirect('training_list')
    
    return render(request, 'add_training.html')

def enroll_list(request):
    enroll = Enrollment.objects.filter(user=request.user )
    return render(request, 'enroll_list.html', {'enrolled_trainings': enroll})


def delete_training(request, training_id):
    training = get_object_or_404(Training, id=training_id)
    if request.method == 'POST':
        training.delete()
        return redirect('training_list')
    return render(request, 'confirm_delete.html', {'training': training})

def enroll_user(request,pk):
    id=Training.objects.get(id=pk)
    user=request.user
    if Enrollment.objects.filter(user=user,course = id):
        messages.error(request,"you're already Enrolled for this Course")
    else:
        Enrollment.objects.create(course = id,user=user)
        messages.success(request,f"Succesfully Enrolled for {id.title} Course")
    return redirect('available_courses')

def available_courses(request):
    courses = Training.objects.all()  # Fetch all courses
    return render(request, 'available_courses.html', {'courses': courses})

def enroll(request):
    if request.method == "POST":
        training_id = request.POST.get("training")
        training = Training.objects.get(id=training_id)

        enrollment, created = Enrollment.objects.get_or_create(user=request.user, training=training)

        if created:
            messages.success(request, f"Successfully enrolled in {training.title}.")
        else:
            messages.error(request, f"You are already enrolled in {training.title}.")

        return redirect("enroll")  # Redirects to the same page

    trainings = Training.objects.all()
    enrolled_trainings = Enrollment.objects.filter(user=request.user)

    return render(request, "enroll.html", {
        "trainings": trainings,
        "enrolled_trainings": enrolled_trainings
    })

