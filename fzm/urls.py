from django.urls import include, path

from . import views

app_name = 'fzm'
urlpatterns = [
    path('', views.index, name='index'),
    path('good/', views.view_good, name='good'),
    path('type/', views.view_type, name='type'),
    path('operate/', views.view_operate, name='operate'),
    path('stock/', views.view_stock, name='stock'),
    path('do/', views.view_do, name='do'),
    path('result/', views.view_result, name='result'),
]
