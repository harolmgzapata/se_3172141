from django.urls import path

from se_core.vistas.navegacion.principal import index, acercade, misionvision, contactanos, iniciarsesion, loginn

urlpatterns = [
    path('index/', index, name='index'),
    path('acerca_de/', acercade, name='acercade'),
    path('mision_y_vision/', misionvision, name='misionyvision'),
    path('contactanos/', contactanos, name='contactanos'),
    path('inicio_de_sesion/', iniciarsesion, name='iniciosesion'),
    path('login/', loginn, name='login'),
]