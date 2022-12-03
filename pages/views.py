from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePage(TemplateView):
    template_name = "pages/home.html"

class ProductsPage(TemplateView):
    template_name = "pages/checkProducts.html"
