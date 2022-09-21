from django.urls import path, include
from . import views
# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('', views.library, name='library'),
    path('addbook/', views.addbook, name='addbook'),
    path('<str:author>/<str:title>/', views.addbook, name='readbook'),
]