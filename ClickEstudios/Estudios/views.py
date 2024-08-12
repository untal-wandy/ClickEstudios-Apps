from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Plan, Servicio, PlanAtributos

# Create your views here.
class DashboardView(TemplateView):
      template_name = 'base/base.html'


class HomeView(TemplateView):
      template_name = 'estudios/home.html'

      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['planes'] = Plan.objects.all()
            context['servicios'] = Servicio.objects.all()
            return context