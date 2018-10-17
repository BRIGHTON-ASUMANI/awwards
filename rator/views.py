from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm, ProjectForm, ProfileForm, CommentForm
from .models import Project, Profile
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    profile = Profile.get_all()
    project=Project.objects.filter(user=request.user)
    current_user= request.user
    commented = CommentForm()
    context = {"project":project,"current_user":current_user,"profile":profile, 'commented':commented}
    return render(request, 'home.html', context )


@login_required(login_url='/login')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')

    else:
        form = ProjectForm()
    return render(request, 'image.html', {"form": form})


@login_required(login_url='/login')
def comment(request,id):
    upload = Image.objects.get(id=id)
    if request.method == 'POST':
        comm=CommentForm(request.POST)
        if comm.is_valid():
            comment=comm.save(commit=False)
            comment.user = request.user
            comment.post=upload
            comment.save()
            return redirect('home')
    return redirect('home')



@login_required(login_url='/login')
def profile(request):
    current_user = request.user
    project=Project.objects.filter(user=request.user)
    if request.method == 'POST':
        form_data = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form_data.is_valid():
            profile = form_data.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('home')

    else:
        form_data = ProfileForm()
    return render(request, 'profile.html', {"form_data": form_data})



def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You have editted your profile' ))
            return redirect('home')

    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form }
    return render(request, 'edit_profile.html',context)


























def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in' ))
            return redirect('home')
        else:
            messages.success(request, ('error logging in - please try again' ))
            return redirect('login')
    else:
        return render(request, 'login.html', {} )

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out' ))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('You have been registered' ))
            return redirect('home')

    else:
        form = SignUpForm()
    context = {'form': form }
    return render(request, 'register.html',context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('You have password has been changed' ))
            return redirect('home')

    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form }
    return render(request, 'change_password.html',context)
