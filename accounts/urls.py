from django.urls import path, include
from accounts import views as accounts_views
app_name = 'accounts'

urlpatterns = [
    path("login", accounts_views.login, name="login"),
    path("logout", accounts_views.logout, name="logout")
]