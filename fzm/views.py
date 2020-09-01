from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView

from .models import Good, Type, StockOperate


@login_required
def index(request):
    return render(request, 'fzm/index.html')


@login_required
def view_good(request):
    good_list = Good.objects.all()
    return render(request, 'fzm/good.html', {
        'good_list': good_list,
    })


@login_required
def view_type(request):
    type_list = Type.objects.all()
    return render(request, 'fzm/type.html', {
        'type_list': type_list
    })


@login_required
def view_operate(request):
    operate_list = StockOperate.objects.order_by('-id')
    return render(request, 'fzm/operate.html', {
        'operate_list': operate_list,
    })


@login_required
def view_stock(request):
    good_list = Good.objects.all()
    return render(request, 'fzm/stock.html', {'good_list': good_list})


@login_required
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


@login_required()
def view_result(request):
    return render(request, 'fzm/result.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
