from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import HomeMotivation, Project, Blog, My, Services

# Create your views here.

class HomeListView(ListView):
    template_name='main/index.html'

    def get(self, request):
        home_motivation = HomeMotivation.objects.all()
        services = Services.objects.all()
        project = Project.objects.filter(active=True)
        blog = Blog.objects.filter(active=True)
        return render(request, self.template_name, {
            'home_motivation':home_motivation,
            'services':services,
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
        article_details = Blog.objects.get(slug=slug)
        return render(request, self.template_name, {
            'article_details':article_details,
        }) 

class ServicesListView(ListView):
    template_name='services/index.html'

    def get(self, request):
        services_list = Services.objects.all()
        return render(request, self.template_name, {
            'services_list':services_list,
        })
            
class ServicesDetailView(DetailView):
    template_name='Services/smm/index.html'

    def get(self, request, slug):
        service_details = Services.objects.get(slug=slug)
        return render(request, self.template_name, {
            'service_details':service_details,
        })