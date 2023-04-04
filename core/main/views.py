from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import HomeMotivation, Project, Blog, My, ServicesAll, Services

# Create your views here.

class HomeListView(ListView):
    template_name='main/index.html'

    def get(self, request):
        home_motivation = HomeMotivation.objects.all()
        services_list = ServicesAll.objects.all()
        project = Project.objects.filter(active=True)
        blog = Blog.objects.filter(active=True)
        return render(request, self.template_name, {
            'home_motivation':home_motivation,
            'services_list':services_list,
            'project':project,
            'blog':blog,
        })
    
class BlogListView(ListView):
    template_name='blog/index.html'

    def get(self, request):
        article_list = Blog.objects.all()
        my_list = My.objects.all()
        return render(request, self.template_name, {
            'article_list':article_list,
            'my_list':my_list,
        })
    
class ArticleDetailView(DetailView):
    template_name='blog/servery/index.html'

    def get(self, request, slug):
        article_details = Blog.objects.filter(pk=slug)
        return render(request, self.template_name, {
            'article_details':article_details,
        }) 

class ServicesListView(ListView):
    template_name='services/index.html'

    def get(self, request):
        services_list = ServicesAll.objects.all()
        return render(request, self.template_name, {
            'services_list':services_list,
        })
            
class ServicesDetailView(DetailView):
    template_name='services/smm/index.html'

    def get(self, request, slug, id):
        service_all = ServicesAll.objects.get(slug=slug)
        service_list = Services.objects.filter(pk=id)
        return render(request, self.template_name, {
                        'id':id,
                      'service_all':service_all,
                      'service_list':service_list,
        })