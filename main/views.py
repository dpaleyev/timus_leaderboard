from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile
from .theme_check import theme_res2

def leaderboard(request):
    data = {}
    data['test'] = []
    for i in Profile.objects.all():
        t = theme_res2(i)
        cnt = 0
        for j in range(len(t)):
            cnt += t[j]['compl']
        data['test'].append([cnt, str(i.user), int(i.user_id)])
    data['test'].sort(reverse=True)

    return render(request, "index.html", context=data)

def user_stats(request, name):
    data = {}
    for i in Profile.objects.all():
        if (int(i.user_id) == name):
            data['name'] = str(i.user)
    return render(request, "profile.html", context=data)

# Create your views here.
