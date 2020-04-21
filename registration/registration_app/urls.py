from django.urls import path
from registration_app import views
from django.conf.urls import url

app_name = 'registration_app'

urlpatterns = [
    path('', views.index, name="index"),
    path('login/index/', views.index, name="index"),
    path('login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('logout/index/', views.index, name="index"),
    path('login/sucess/', views.sucess, name="sucess"),
]


