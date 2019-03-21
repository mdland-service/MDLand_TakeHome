from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login-home'),
    path('create_acc/', views.create_acc, name='create-acc'),
]