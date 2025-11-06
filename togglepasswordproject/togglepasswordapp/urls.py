from django.urls import path
from . import views

urlpatterns = [
    
    path("",views.login,name='login'),
    path('register/', views.register_view, name='register'),
    path('success/', views.success, name='success'),
    path('profileview/', views.profile_view, name='profileview'),
    path('editprofile/', views.edit_profile, name='editprofile'),
    
]