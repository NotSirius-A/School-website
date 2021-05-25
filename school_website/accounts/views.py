from django.contrib.auth import authenticate, login, logout
from .forms import AuthenticationFormCustom
from django.shortcuts import redirect, render

def login_page_view(request, *args, **kwargs):
    """Django view,
    display a page with login form and login the user
    """


    user = None
    form = AuthenticationFormCustom(data=request.POST or None)

    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)

        return redirect(request.GET['next'])

    context = {
        'form': form,
        'user': user,
    }

    return render(request, 'accounts/login_page.html', context=context)
