
# Arquivo com caminhos das URLs do Blog.

from django.urls import path
from blog import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
]