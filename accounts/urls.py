from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from accounts.views import Login, Cadastro, UpdateUsuario, ProfilePage
from accounts import views as acc_views
app_name = 'accounts'

urlpatterns = [
     path('login/', Login.as_view(), name='login'),
     path('logout/', auth_views.LogoutView.as_view(), name="logout"),
     path('cadastro/', Cadastro.as_view(), name="cadastro"),
     path('editUser/<int:pk>', UpdateUsuario.as_view(), name="editar"),
     path('perfil/<int:pk>', ProfilePage.as_view(), name="perfil"),
     path("gerar_relatorio", acc_views.gerar_relatorio, name="gerar_relatorio"),
     path('reset_password/', auth_views.PasswordResetView.as_view(
          template_name="accounts/password_reset.html",
          success_url=reverse_lazy('accounts:password_reset_done')
          ), 
          name="reset_password"),
     path('password_reset_sent',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
         name="password_reset_done"),
     path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
         name="password_reset_confirm"),
     path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
         name="password_reset_complete")
]