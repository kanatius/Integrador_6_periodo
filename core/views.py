from django.views.generic import TemplateView


class index_page(TemplateView):
    template_name = 'index.html'
