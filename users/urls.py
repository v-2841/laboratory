from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
)
from django.urls import path, reverse_lazy


app_name = 'users'
urlpatterns = [
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logout.html'),
        name='logout'
    ),
    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='users/password_change_form.html',
            success_url=reverse_lazy('users:password_change_done'),
        ),
        name='password_change_form'
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html'
        ),
        name='password_change_done'
    )
]
