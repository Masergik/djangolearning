from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class HomeView(View):
    template_name = 'testapp/index.html'

    def get(self, request):
        return render(request, self.template_name)


class DeliveryView(TemplateView):
    template_name = 'testapp/delivery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'delivery_name': 'Новая почта',
            'city': 'Харьков',
            'department': 'Отделение №7 (ул. пр.Победы, 46-а)',
            # 'id': self.kwargs['user_id']
        })
        return context
