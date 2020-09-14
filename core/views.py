from django.views.generic import TemplateView, ListView

from .models import PhrasesModel


class HomeView(ListView):
    template_name = 'index.html'
    model = PhrasesModel
    context_object_name = 'phrases'


class ElementosView(TemplateView):
    template_name = 'elements.html'



