from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print(username, password)
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            print('form.is_valid')
            user = form.get_user()
            auth.login(request, user)
            return HttpResponseRedirect("/")
        print('NOT form.is_valid')
    else:
        form = AuthenticationForm()

    return render(request, "generic/login.html", {
        'form': form,
    })
    #username = request.POST.get('username', '')
    #password = request.POST.get('password', '')
    #if all((username, password)):
        #user = auth.authenticate(username=username, password=password)
        #if user is not None and user.is_active:
            ## Correct password, and the user is marked "active"
            #auth.login(request, user)
            ## Redirect to a success page.
            #return HttpResponseRedirect("/")


def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")
