from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    # path('deshboard/', views.deshboard, name='deshboard'),

    path('activate/<uidb64>/<token>/', views.activate, name='activate')
]
