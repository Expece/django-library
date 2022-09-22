from django.urls import path, include
from . import views
# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('', views.library, name='library'),
    path('addbook/', views.addbook, name='addbook'),
    path('<str:book_author>/<str:book_title>', views.readbook, name='readbook'),
    path('<str:category_title>', views.getBooksByCategory, name='getBooksByCategory'),
]