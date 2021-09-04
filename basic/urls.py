from django.urls import path 
from django.conf.urls import url
from .views import SchoolListViews, SchoolDetailView
from basic import views

app_name = "basic_app"
urlpatterns = [
    url(r'^$', views.SchoolListViews.as_view(), name='list'),
    url(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(),name='detail'),
]