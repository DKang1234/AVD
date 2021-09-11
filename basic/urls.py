from django.urls import path 
from django.conf.urls import url
from .views import SchoolListViews, SchoolDetailView, SchoolDetailUpdateView, SchoolDetailDeleteView, SchoolDetailCreateView
from basic import views

app_name = "basic_app"
urlpatterns = [
    url(r'^$', views.SchoolListViews.as_view(), name='list'),
    url(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(),name='detail'), 
    url(r'^create/$', SchoolDetailCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', SchoolDetailUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', SchoolDetailDeleteView.as_view(), name='delete'),
  ]