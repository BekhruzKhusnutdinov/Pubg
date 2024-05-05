from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .forms import RegisterForm
from django.contrib import messages
from .models import *


# Create your views here.

class MainList(ListView):
    model = Product
    context_object_name = 'categories'
    extra_context = {
        'title': 'Главная страница'
    }
    template_name = 'shop/index.html'


def final(request):
    return render(request, 'shop/final.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('final')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, 'shop/login_register.html', context)
