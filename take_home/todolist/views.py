from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Todo, mylist
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

##Index/homepage. Create or delete lists. Shows all lists associated with user.
@login_required(login_url='/')
def index(request):
    current_user = request.user
    user_lists = mylist.objects.filter(user=current_user)
    return render(request, 'todolist/index.html', {'user_lists':user_lists,'current_user':current_user})

@login_required(login_url='/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')

@login_required(login_url='/')
def createlist(request):
    if request.method == 'POST':
        user = request.user
        new_list = mylist(listname = request.POST['listname'], user=user)
        new_list.save()
        return redirect ('/index')
    else:
        return redirect ('/index')

@login_required(login_url='/')
def dellist(request, list_id):
    if request.method=='POST':
        deletable = mylist.objects.get(id=list_id)
        deletable.delete()
        return redirect('/index')
    else:
        return redirect('/index')


##To do lists. Add or delete to-dos. Show all to-dos associated with the corresponding to do list.
@login_required(login_url='/')
def tdldetails(request, list_id):
    tdlist = mylist.objects.get(id=list_id)
    current_user = request.user
    user_todo = Todo.objects.filter(user=current_user, whichlist=tdlist)
    return render(request, 'todolist/tdlists.html', {'tdlist': tdlist, 'todos': user_todo,'list_id':list_id})

@login_required(login_url='/')
def addtodo(request):
    if request.method == 'POST':
        user = request.user
        list_id = request.POST.get('list_id')
        Todo.objects.create(todoname=request.POST['todoname'], user=user, whichlist_id=list_id)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/')
def deltodo(request, todo_id):
    if request.method=='POST':
        deletable = Todo.objects.get(id=todo_id)
        deletable.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

