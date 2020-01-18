from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class home(TemplateView):
    template_name = "basicapp/home.html"

class about(TemplateView):
    template_name = "basicapp/about.html"

class projects(TemplateView):
    template_name = "basicapp/projects.html"

class portfolio(TemplateView):
    template_name = "basicapp/portfolio.html"

class contacts(TemplateView):
    template_name = "basicapp/contacts.html"
