from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('product/<int:product_id>/', views.product_view, name='product'),
    path('category/<category_slug_name>/', views.category_view, name='category'),
    path('collection/<collection_slug_name>/', views.collection_view, name='collection'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
