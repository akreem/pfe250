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
    #path('l3vpn_ospf/', views.l3vpn_ospf, name='l3vpn_ospf'),
    #path('l3vpn_rip/', views.l3vpn_rip, name='l3vpn_rip'),
    #path('l3vpn_eigrp/', views.l3vpn_eigrp, name='l3vpn_eigrp'),
    path('create_vrf/<str:client>/', views.creation_vrf, name='create_vrf'),
    path('client_rip/', views.client_rip, name='client_rip'),
    path('client_ospf/', views.client_ospf, name='client_ospf'),
    path('client_eigrp/', views.client_eigrp, name='client_eigrp'),
    path('changepassword/', views.changepassword, name='changepassword'),
]
