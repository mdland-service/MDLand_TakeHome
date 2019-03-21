from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

##Login landing page. Requires user to login or create account before accessing to-do lists.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/index')
    else:
        form = AuthenticationForm ()
    return render(request, 'login/home.html', {'form':form})

def create_acc(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm ()
    return render(request, 'login/create_acc.html', {'form': form})
