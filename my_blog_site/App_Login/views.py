from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UserSignup,UserProfileChange,UserProfilePic
# Create your views here.
from .models import UserProfile


def signup(request):
    form = UserSignup()
    created = False
    if request.method == 'POST':
        form = UserSignup(request.POST)
        if form.is_valid():
            form.save()
            created = True
    dict = {'form':form ,'created':created}
    return render(request,'App_Login/signup.html',dict)

def signin(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
    dict = {'form': form}
    return render(request,'App_Login/signin.html',dict)

@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('signin'))

@login_required
def profile(request):
    return render(request,'App_Login/profile.html')

@login_required
def changeUserInfo(request):
    current_user = request.user
    form  = UserProfileChange()
    if request.method == 'POST':
        form = UserProfileChange(request.POST,instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)
    dict = {'form':form}
    return render(request,'App_Login/changeUserInfo.html',dict)

@login_required
def changePassword(request):
    current_user = request.user
    form = PasswordChangeForm(current_user)
    success = False
    if request.method == 'POST':
        form = PasswordChangeForm(current_user,data=request.POST)
        if form.is_valid():
            form.save()
            success = True
    dict = {'form':form,'success':success}
    return render(request,'App_Login/changePassword.html',dict)

def change_profile(request):
    form = UserProfilePic
    if request.method == 'POST':
        form = UserProfilePic(request.POST,request.FILES)
        current_user = form.save(commit=False)
        current_user.user = request.user
        current_user.save()
        return HttpResponseRedirect(reverse('profile'))

    dict = {'form':form}
    return render(request,'App_Login/change_profile.html',dict)

@login_required
def update_profile_pic(request):
    form = UserProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = UserProfilePic(request.POST,request.FILES,instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    dict = {'form':form}
    return render(request,'App_Login/change_profile.html',dict)