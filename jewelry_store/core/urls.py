from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from core.views import HomeView, DeliveryView, IndexView, ContactUsView

from core.views import AddProductView
from core import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('email-sent/', ContactUsView.as_view(template_name='core/email-sent.html')),
    path('', IndexView.as_view(), name='index_class'),
    path('contact/', TemplateView.as_view(template_name='core/contact.html')),
    # path('', HomeView.as_view(), name='homeview'),
    path('delivery/', DeliveryView.as_view(), name='deliveryview'),
    path('add-product/', AddProductView.as_view()),
    path('contact-us/', ContactUsView.as_view(), name='contact_us')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
