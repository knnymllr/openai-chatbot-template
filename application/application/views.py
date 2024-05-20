from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            # return redirect('/dashboard') # TODO
            return redirect('/chat')
    else: 
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# ! Move to /chat/logout
@login_required(redirect_field_name=None)
def logout(request):
    auth.logout(request)
    return redirect('login')