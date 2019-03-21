from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('logout', views.logout_view, name='logout'),
    path('createlist',views.createlist, name='createlist'),
    path('todolist/dellist/<int:list_id>', views.dellist, name='dellist'),
    path('todolist/<int:list_id>', views.tdldetails, name='tdldetails'),
    path('todolist/addtodo', views.addtodo, name='addtodo'),
    path('todolist/deltodo/<int:todo_id>', views.deltodo, name='deltodo')
]
