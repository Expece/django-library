from django.urls import path
from . import views


urlpatterns = [
    path('', views.Library.as_view(), name='library'),
    path('addbook/', views.AddBook.as_view(), name='addbook'),
    path('book/<slug:book_slug>', views.BookPage.as_view(), name='BookPage'),
    path('category/<slug:category_slug>', views.BooksByCategory.as_view(), name='BooksByCategory'),
    path('search/', views.Search.as_view(), name='search'),
]