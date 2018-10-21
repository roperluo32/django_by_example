from django.urls import path
# from .views import login_request

from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import change_password
from django.contrib.auth.views import change_password_done
from django.contrib.auth.views import reset_password
from django.contrib.auth.views import reset_password_done
from django.contrib.auth.views import reset_password_comfirm
from django.contrib.auth.views import reset_password_complete

app_name = 'account'
urlpatterns = [
    path('login/', login, name='login'),
]
