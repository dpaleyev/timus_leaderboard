from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile
from .task_update import *
from .forms import NewUserForm, CreateProfile
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def leaderboard(request):
    data = {}
    data['test'] = []
    for i in Profile.objects.all():
        # update(i)
        data['test'].append([len(i.completed_tasks.values_list()), str(i.user), int(i.user_id)])
    data['test'].sort(reverse=True)

    return render(request, "index.html", context=data)

def user_stats(request, name):
    data = {}
    for i in Profile.objects.all():
        if (int(i.user_id) == name):
            data['name'] = str(i.user)
    return render(request, "profile.html", context=data)

def reg_req(request):
    if (request.method == "POST"):
        form = NewUserForm(request.POST)
        # print(request.POST)
        # print(form.errors)
        # print(request.POST['judge_id'])
        if (form.is_valid() and request.POST['judge_id'].isdigit()):
            user = form.save()
            login(request, user)
            p = Profile(user=user, judge_id=int(request.POST['judge_id']))
            p.save()
            update(p)
            return redirect('/')
        else:
            _form = NewUserForm()
            _formJ = CreateProfile()
            if (not request.POST['judge_id'].isdigit() and form.is_valid()): return render(request, "reg.html", context={'reg_form': _form, 'get_id_form': _formJ, 'error': 'Invalid Judge_ID'})
            else: return render(request, "reg.html", context={'reg_form': _form, 'get_id_form': _formJ, 'error': form.errors})
    form = NewUserForm()
    formJ = CreateProfile()
    return render(request, "reg.html", context={'reg_form': form, 'get_id_form': formJ, 'error': ''})

def log_req(request):
    if (request.method == "POST"):
        form = AuthenticationForm(request, data=request.POST)
        if (form.is_valid()):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if (user is not None):
                login(request, user)
                return redirect('/')
            return render(request, "login.html", context={'log_form': form, 'errors': "Invalid data"})
        return render(request, "login.html", context={'log_form': form, 'errors': "Invalid data"})
    form = AuthenticationForm()
    return render(request, "login.html", context={'log_form': form, 'errors': ''})

def logout_req(request):
    logout(request)
    return redirect("/")

# Create your views here.
