from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.library, name='library'),
    path('new_book/', views.new_book, name='new_book'),
    path('<str:author>/<str:title>', views.reader, name='reader'),
    path('search/', views.search, name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)