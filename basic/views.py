from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

class SchoolListViews(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = "basic_app/school_list.html"

class SchoolDetailView(DetailView):
    context_object_name = 'schools_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html' 




