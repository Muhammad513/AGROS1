from django.contrib import admin
from django.urls import path,include
from .views import*
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', homePage,name="home"),
    path('reestr/',reestr_P,name='reestr'),
    path('Paxta/',PaxtaX,name="paxta"),
    path('xarajat/',xarajat_p,name="xarajat"),
    path('hudud/',hudud_p,name="hudud_p"),
    #-----------------------------------------
    path('Galla/',GallaX,name="galla"),
    path('reestrg/',reestrg,name='reestrg'),
    path('Ombor/',omborG,name='omborG'),
    path('hududg/',hududg,name='hududg'),

    path('testing/',testing,name="testing"),
    path('xarajatG/',xarajatG,name="xarajatG"),
    #-----------------------------------------
    path('naryad/',naryad,name="naryad"),


    #------------------------------------------
    path('chat/',chat,name="chat"),
    path('chat/<str:pk>',chatreq,name='chatreq') 

]

