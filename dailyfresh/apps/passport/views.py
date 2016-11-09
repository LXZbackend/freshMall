from django.views.decorators.http import require_http_methods, require_POST, require_GET
from django.contrib.auth import authenticate
from django.contrib.auth import login as _login
from django.contrib.auth import logout as _logout
from utils.views import json_view
from django.contrib.auth.decorators import login_required
from apps.tasks.tasks import register_success_email
from django.shortcuts import render, redirect
from django.db import transaction
from .models import Passport


@require_http_methods(["GET", "POST"])
def login(request):
    """
    登录
    """
    if request.method == 'GET':
        return render(request, "login.html", {'error':False})
    else:
        username = request.POST['username']
        password = request.POST['pwd']
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            _login(request, user)
            return redirect('/')
        else:
            return render(request, "login.html", {'error':True})


@login_required
@require_GET
def logout(request):
    """
    登出
    """
    _logout(request)
    return redirect('/')


@require_http_methods(["GET", "POST"])
def register(request):
    """
    注册
    """
    if request.method == 'GET':
        return render(request, "register.html")
    else:
        username = request.POST['user_name']
        password = request.POST['pwd']
        email = request.POST.get('email', None)
        with transaction.atomic():
            Passport.create_one_passport(username, email, password)
            user = authenticate(username=username, password=password)
            _login(request, user)
        register_success_email.delay(username, email)
        return redirect('/')
