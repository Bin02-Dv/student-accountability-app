from django.shortcuts import render, redirect
from .models import Goal, Progress
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def logout(request):
    auth.logout(request)
    return redirect('/')

def home(request):
    user = request.user
    return render(request, 'home.html', {'user': user})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successfully...')
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials!!!")
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['cpassword']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!!")
        elif confirm_password != password:
            messages.error(request, "Password and confirm password missed match!!")
        else:
            new_user = User.objects.create_user(username=username, password=password, first_name=fullname)
            new_user.save()
            messages.success(request, "Registration completed successfully...")
            return redirect('login')
    return render(request, 'register.html')

update = False

@login_required(login_url='login')
# View for students to create goals
def create_goal(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        deadline = request.POST['deadline']
        new_goal = Goal(title=title, description=description, created_by=request.user, deadline=deadline)
        new_goal.save()
        messages.success(request, 'Goal Created successfully...')
        return redirect('home')
    return render(request, 'create_goal.html')

@login_required(login_url='login')
# View for tracking progress
def track_progress(request):
    user = request.user
    goals = Goal.objects.filter(created_by=user)
    return render(request, 'track_progress.html', {'goals': goals})

@login_required(login_url='login')
# View for tracking progress
def track_progress_2(request):
    goals = Goal.objects.all()
    return render(request, 'track_student_progress.html', {'goals': goals})


def goal_delete(request, id):
    goal = Goal.objects.get(id=id)
    goal.delete()
    return redirect('track_progress')

@login_required(login_url='login')
# View for students to create goals
def update_goal(request, id):
    update = True
    if request.method == 'POST':
        description = request.POST['description']
        new_goal = Goal.objects.get(id=id)
        new_goal.description = description
        new_goal.status = True
        new_goal.save()
        messages.success(request, 'Goal Updated successfully...')
        return redirect('track_progress')
    return render(request, 'create_goal.html', {'update': update})
