from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('biometric/', views.biometric, name='biometric'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('chat/', views.chat, name='chat'),
    path('setbiometric/', views.set_biometric_security, name='set_biometric_security'),
    path('getbiometric/', views.get_biometric_security, name='get_biometric_security'),
]
