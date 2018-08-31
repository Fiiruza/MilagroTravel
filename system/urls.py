from django.urls import path
from . import views

# Must be deleted in production
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomePage.as_view()),
    path('api/', views.NewsApi.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)