from django.urls import path 
from .views import SchoolListViews

app_name = "basic_app"
urlpatterns = [
    path('list/', SchoolListView.as_view(), name='list')
]