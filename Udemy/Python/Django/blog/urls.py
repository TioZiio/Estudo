
# Arquivo com caminhos das URLs do Blog.

from django.urls import path
from blog import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('exemplo/', views.exemplo, name='exemplo'),
]