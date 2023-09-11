from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('libros/', views.libros, name='libros'),
    path('destacados/', views.destacados, name='destacados'),
    path('reseñas/', views.reseñas, name='reseñas'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),

]
