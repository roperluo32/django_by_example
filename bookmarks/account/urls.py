from django.urls import path
from .views import dashboard

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChange
from django.contrib.auth.views import ChangePasswordDone
# from django.contrib.auth.views import LogoutThenLoginView
# from django.contrib.auth.views import logout
# from django.contrib.auth.views import change_password
# from django.contrib.auth.views import change_password_done
# from django.contrib.auth.views import reset_password
# from django.contrib.auth.views import reset_password_done
# from django.contrib.auth.views import reset_password_comfirm
# from django.contrib.auth.views import reset_password_complete

# from django.contrib.auth.views import Login

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('change-password/done', ChangePasswordDone.as_view(), name='change-password-done'),
    # path('logout_then_login/', LogoutThenLoginView.as_view(), name='login_then_login'),
]
