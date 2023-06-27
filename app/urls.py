from django.urls import path
from . import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'app'
urlpatterns = [
    path('', chat_views.chatPage, name='chat-page'),
    path('auth/login', LoginView.as_view(
        template_name='app/LoginPage.html'
    ), name='login-user'),
    path('auth/logout', LogoutView.as_view(), name='logout-user')
]
