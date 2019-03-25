from django.views.generic import TemplateView
from .models import Price_list, Price

class PricesPageView(TemplateView):

    template_name = "prices/prices.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['price_lists'] = Price_list.objects.all()
        context['prices'] = Price.objects.all()
        return context

