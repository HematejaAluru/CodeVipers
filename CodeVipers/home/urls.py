from django.urls import path,include
from . import views
from .views import chatroom
from blog.views import create,createreply
from . import views
urlpatterns=[
    path('home',views.home,name='home'),
    path('',views.test,name="test"),
    path('login',views.login,name="login"),
    path('login2',views.login2,name="login2"),
    path('test',views.testee,name="test"),
    path('registers',views.registers,name='registers'),
    path('tester',views.tester,name="tester"),
    path('neuralnetworks',views.neural,name="neuralnetworks"),
    path('forgotpass',views.forgotpass,name="forgotpass"),
    path('temp',views.temp,name='temp'),
    path('roomname',views.roomname,name='roomname'),
    path('/chat/' + chatroom +'/' +'parallel',views.parallel,name='parallel'),
    path('create',create,name='create' ),
    path('ideer',views.ideer,name='ideer'),
    path('createreply',createreply,name='createreply'),
    path('r',views.r,name='r'),
]