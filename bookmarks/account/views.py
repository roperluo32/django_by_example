from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

# def login_request(request):
#     if request.method == 'POST':
#         login_form = LoginForm(request.POST)
#         if login_form.is_valid():
#             cd = login_form.cleaned_data
#             user = authenticate(username=cd['username'],
#                                 password=cd['password'])
#             if user != None:
#                 login(request, user)
#                 return HttpResponse('Authenticate successfully.')
#             else:
#                 return HttpResponse('Authenticate failed.')
#         else:
#             return HttpResponse('login form data is valid.')
#     else:
#         login_form = LoginForm()

#     return render(request, 'account/login.html', {'login_form': login_form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html',
                    {'section': 'dashboard'})