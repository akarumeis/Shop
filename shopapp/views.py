from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login
from .models import Product, Comment
# Create your views here.
def show_reg_form(request):
    context = {}
    if request.method == "POST": 
        login = request.POST.get("login")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        context["login"] = login
        context["password"] = password
        context["password_confirm"] = password_confirm
        if password == password_confirm:
            try:
                User.objects.create_user(username = login, password = password)
                return redirect('shop')
            except IntegrityError:
                context['error'] = 'Користувач вже існує' 
        else:
            context["error"] = "Паролі не спiвпадають"
    return render(request, 'reg_form.html', context=context)

def show_log_form(request):
    context = {}
    if request.method == 'POST':
        login_user = request.POST.get("login")
        password = request.POST.get("password")
        user = authenticate(request, username = login_user, password = password)
        if user != None:
            login(request, user)
            return redirect('shop')
        else:
            
            context['error'] = 'Логін або пароль невірні'
            
    else:    
        return render(request, 'log_form.html', context)
    
    
def show_shop(request):
    if request.user.is_authenticated:
        context = {
            "products":Product.objects.all(),
            "comments":Comment.objects.all()
            }
        if request.method == "POST":
            author = request.POST.get("author")
            text = request.POST.get("text")
            Comment.objects.create(author = author, text = text)
            return redirect('shop')
        return render(request, 'shop.html', context=context)
    else:
        return redirect('log_form')