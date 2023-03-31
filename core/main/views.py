from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import HomeMotivation, Project, Blog, Service, My

# Create your views here.

class HomeListView(ListView):
    template_name='main/index.html'

    def get(self, request):
        home_motivation = HomeMotivation.objects.all()
        service = Service.objects.all()
        project = Project.objects.filter(active=True)
        blog = Blog.objects.filter(active=True)
        return render(request, self.template_name, {
            'home_motivation':home_motivation,
            'service':service,
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