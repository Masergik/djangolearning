from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('cart_adding/', views.cart_adding_view, name='cart_adding'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('cart/', views.cart_view, name='cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
