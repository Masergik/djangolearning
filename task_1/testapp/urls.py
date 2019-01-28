from django.urls import path
from django.views.generic import TemplateView
from testapp.views import HomeView, DeliveryView

urlpatterns = [
    path('contact/', TemplateView.as_view(template_name='testapp/contact.html')),
    path('', HomeView.as_view(), name='homeview'),
    path('delivery/', DeliveryView.as_view(), name='deliveryview'),
]