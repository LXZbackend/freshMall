from django.shortcuts import render

# Create your views here.


def index(request):
	return render(request, 'freshMall/index.html')


def login(request):
	return render(request, 'freshMall/login.html')


def cart(request):
	return render(request, 'freshMall/cart.html')


def user_center_order(request):
	return render(request, 'freshMall/user_center_order.html')


def register(request):
	return render(request, 'freshMall/register.html')
