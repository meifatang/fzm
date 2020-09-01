from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView

from .models import Good, Type, StockOperate


def index(request):
    good_list = Good.objects.all()
    type_list = Type.objects.all()
    operate_list = StockOperate.objects.order_by('-id')
    return render(request, 'fzm/index.html', {
        'good_list': good_list,
        'type_list': type_list,
        'operate_list': operate_list,
    })


def view_good(request):
    good_list = Good.objects.all()
    return render(request, 'fzm/good.html', {
        'good_list': good_list,
    })


def view_type(request):
    type_list = Type.objects.all()
    return render(request, 'fzm/type.html', {
        'type_list': type_list
    })


def view_operate(request):
    operate_list = StockOperate.objects.order_by('-id')
    return render(request, 'fzm/operate.html', {
        'operate_list': operate_list,
    })


def view_stock(request):
    good_list = Good.objects.all()
    return render(request, 'fzm/stock.html', {'good_list': good_list})


def view_do(request):
    select = request.POST['select']
    count = request.POST['count']

    good = get_object_or_404(Good, pk=select)

    print(good.good_name)

    good.quantity += int(count)
    good.save()

    StockOperate.objects.create(the_time=timezone.now(), good=good, operate_quantity=count)

    messages.info(request, '操作成功')

    good_list = Good.objects.all()
    return render(request, 'fzm/result.html')


def view_result(request):
    return render(request, 'fzm/result.html')


def view_login(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        authenticate()
    return render(request, 'fzm/login.html')


def view_register(request):
    return render(request, 'fzm/register.html')


def view_password(request):
    return render(request, 'fzm/password.html')


