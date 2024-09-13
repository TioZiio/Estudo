
# Arquivo com caminhos das URLs do Blog.

from django.urls import path
from home import views


urlpatterns = [
    path('', views.home),
]