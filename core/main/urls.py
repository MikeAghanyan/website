from django.urls import path
from . import views

urlpatterns = [    
    path('', views.HomeListView.as_view(), name='main'),
    path('blog', views.BlogListView.as_view(), name='blog'),
    path('', views.article, name='blog'),


]