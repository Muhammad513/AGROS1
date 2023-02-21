from django.contrib import admin
from django.urls import path,include
from .views import*
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', infors,name="ihome"),
    path('paxtasuv/', p_suv,name="p_suv"),
    path('gallasuv/', g_suv,name="g_suv"),
    path('chigit/', chigit,name="chigit"),
    path('oq_o/', oq_olish,name="oq_olish"),
    path('oq_k/', oq_komish,name="oq_komish")
    
]
