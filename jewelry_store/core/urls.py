from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView
from core.views import IndexView, ContactUsView, RegistrationView, LoginView

from core.views import AddProductView, HomeView, DeliveryView
from core import views


urlpatterns = [
    path('', IndexView.as_view(), name='index_class'),
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
    path('email-sent/', ContactUsView.as_view(template_name='core/email-sent.html')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('contact/', TemplateView.as_view(template_name='core/contact.html')),
    # path('', HomeView.as_view(), name='homeview'),
    path('delivery/', DeliveryView.as_view(), name='deliveryview'),
    path('add-product/', AddProductView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
