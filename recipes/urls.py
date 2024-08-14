from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = "recipes"

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:id>/', views.recipe, name='recipe')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # for serving media files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # for serving static files