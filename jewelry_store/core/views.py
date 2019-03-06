# from django.db.models import Q
from datetime import datetime, time, date, timedelta

from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from core.forms import AddProductForm
from store.models import Product, ProductImage


# def index(request):
#     products_images = ProductImage.objects.filter(is_active=True, is_main_img=True)
#     products_images_rings = products_images.filter(product__category__name='Кольца')
#     products_images_earrings = products_images.filter(product__category__name__in=['Серьги', 'Пусеты'])
#     new_products = products_images.order_by('-created')[:3]
#
#     return render(request, 'core/index.html', locals())


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products_images = ProductImage.objects.filter(is_active=True, is_main_img=True).select_related('product')\
            .select_related('product__sale_percent')
        products_images_rings = products_images.filter(product__category__name='Кольца')
        products_images_earrings = products_images.filter(product__category__name__in=['Серьги', 'Пусеты'])
        new_products = products_images.order_by('-created')[:3]

        context.update({
            'products_images': products_images,
            'products_images_rings': products_images_rings,
            'products_images_earrings': products_images_earrings,
            'new_products': new_products
        })
        return context


class CategoryView(ListView):
    template_name = 'core/category.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        return self.model.objects.filter(category='Серьги')


class HomeView(View):
    template_name = 'core/index.html'

    def get(self, request):
        return render(request, self.template_name)

    # def get_queryset(self):
    #     return self.model.objects.filter(
    #         Q(rating=10) | Q(type=Post.TYPE_MATURE)
    #     ).distinct()


class DeliveryView(TemplateView):
    template_name = 'core/delivery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'delivery_name': 'Новая почта',
            'city': 'Харьков',
            'department': 'Отделение №7 (ул. пр.Победы, 46-а)',
            # 'id': self.kwargs['user_id']
        })
        return context


class AddProductView(TemplateView):
    template_name = 'core/add_product.html'

    def get_context_data(self, **kwargs):
        context = super(AddProductView, self).get_context_data(**kwargs)
        context['form'] = AddProductForm()
        return context
