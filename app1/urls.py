from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('results/', views.results, name='results'),
    path('setinterface/', views.set_interface, name='set_interface'),
    path('changehostname/', views.changehostname, name='changehostname'),
    path('eigrp/', views.eigrp, name='eigrp'),
    path('ospf/', views.ospf, name='ospf'),
    path('rip/', views.rip, name='rip'),
]
