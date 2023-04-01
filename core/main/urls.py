from django.urls import path
from . import views

urlpatterns = [    
    path('', views.HomeListView.as_view(), name='main'),
    path('blog', views.BlogListView.as_view(), name='blog'),
    path('blog/<slug:slug>', views.ArticleDetailView.as_view(), name='article'),
    path('services', views.ServicesListView.as_view(), name='services'),
    path('services/<slug:slug>', views.ServicesDetailView.as_view(), name='service_details'),    
]