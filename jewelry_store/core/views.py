# from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, FormView

from core.forms import AddProductForm, ContactUsForm, RegistrationForm, LoginForm
from store.models import Product, ProductImage, Category, Collection

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
        categories = Category.objects.all()
        collections = Collection.objects.all()

        context.update({
            'categories': categories,
            'collections': collections,
            'products_images': products_images,
            'products_images_rings': products_images_rings,
            'products_images_earrings': products_images_earrings,
            'new_products': new_products
        })
        return context


class ContactUsView(FormView):
    template_name = 'core/contact-us.html'
    form_class = ContactUsForm
    success_url = '/email-sent/'

    def form_valid(self, form):
        # store_email = ['masergineer@gmail.com']
        store_email = ['test.sg.jewelry@gmail.com']
        sender_email = form.cleaned_data['sender_email']
        subject = form.cleaned_data['subject']
        message = "{name} / {sender_email} / {phone} said: ".format(
            name=form.cleaned_data['name'],
            sender_email=form.cleaned_data['sender_email'],
            phone=form.cleaned_data['phone'])
        message += "\n\n{0}".format(form.cleaned_data['message'])

        send_mail(subject, message, sender_email, store_email)

        return super(ContactUsView, self).form_valid(form)


class LoginView(View):
    template_name = 'core/login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        context = {'form': form}
        return render(self.request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(self.request, user)
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(self.request, self.template_name, context)


def logout_view(request):
    logout(request)
    return render(request, 'core/logout.html')


class RegistrationView(View):
    template_name = 'core/registration.html'

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        context = {'form': form}
        return render(self.request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            city = form.cleaned_data['city']
            new_user.save()
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(self.request, self.template_name, context)


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
