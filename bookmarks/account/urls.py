from django.urls import path
from .views import login_request

app_name = 'account'
urlpatterns = [
    path('login/', login_request, name='login'),
]
