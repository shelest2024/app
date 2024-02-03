from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from carts.models import Cart
from orders.models import Order, OrderItem
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


# Авторизация
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username  = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                    
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {
        'title':'Совенок - Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', context)

# Регистрация
def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()
    
    context = {
        'title':'Совенок - Регистрация',
        'form': form,
    }
    return render(request, 'users/registration.html', context)


# Профиль
# Проверка на авторизацию
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профайл успешно обновлен")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    orders = Order.objects.filter(user=request.user).prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product"),
                )
            ).order_by("-id")
        

    context = {
        'title': 'Home - Кабинет',
        'form': form,
        'orders': orders,
    }
    return render(request, 'users/profile.html', context)

def users_cart(request):
    return render(request, 'users/users_cart.html')


# Контроллер под корзину пользователя
def users_cart(request):
    return render(request, 'users/users_cart.html')


# Выход из системы
# Проверка на авторизацию
@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))

