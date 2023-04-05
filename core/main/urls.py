from django.urls import path
from . import views

urlpatterns = [    
    path('', views.HomeListView.as_view(), name='main'),
    path('blog', views.BlogListView.as_view(), name='blog'),
    path('projects', views.ProjectsListView.as_view(), name='projects'),
    path('services', views.ServicesListView.as_view(), name='services'),
    path('services/smm', views.smm, name='smm' ),
    path('services/online-store', views.onlinestore, name='online-store' ),
    path('services/website', views.website, name='website' ),
    path('blog/servers', views.servers, name='servers' ),
    path('blog/seo', views.seo, name='seo' ),
    path('blog/why-u-need-a-website', views.whyuneedawebsite, name='why-u-need-a-website' ),
    path('blog/brand', views.brand, name='brand' ),
    # path('cv/', views.cv_view, name='cv'),
    # path('blog/<slug:slug>', views.ArticleDetailView.as_view(), name='article'),
    # path('services/<slug:slug>', views.ServicesDetailView.as_view(), name='service_details'),    
]