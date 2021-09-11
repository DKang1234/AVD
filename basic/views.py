from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView
from . import models
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

class SchoolListViews(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = "basic_app/school_list.html"

class SchoolDetailView(DetailView):
    context_object_name = 'schools_details'
    model = models.School
    template_name = 'basic_app/school_detail.html' 

class SchoolDetailCreateView(CreateView):
    model = models.School

class SchoolDetailUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDetailDeleteView(DeleteView):
    fields = ('name', 'principal')
    model = models.School






