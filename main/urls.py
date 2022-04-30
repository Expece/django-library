from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('library/', views.library, name='library'),
    path('about/', views.about, name='about'),
    path('library/book/<int:pk>/', views.reader, name='reader'),
    path('library/new_book/', views.new_book, name='new_book'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
