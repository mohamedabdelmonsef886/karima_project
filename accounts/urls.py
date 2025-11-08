from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register_view, name='register'),  # أضف view للتسجيل
    path('dashboard/', views.dashboard, name='dashboard'),
path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # أضف ده هنا! (next_page عشان يرجع للرئيسية بعد الخروج)
]
