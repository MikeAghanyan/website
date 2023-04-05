from django.shortcuts import render
from django.http import FileResponse
from django.views.generic import ListView
from .models import HomeMotivation, ProjectCategory, ServiceCategory, BlogCategory, CV

# Create your views here.

# def cv_view(request):
#     cv = CV.objects.get(pk=1)  
#     response = FileResponse(open('media/WebDev_CV.pdf'), content_type='application/pdf')
#     return response

class HomeListView(ListView):
    template_name='main/index.html'

    def get(self, request):
        home_motivation = HomeMotivation.objects.all()
        project_list = ProjectCategory.objects.all()
        service_list = ServiceCategory.objects.all()
        blog_list = BlogCategory.objects.filter(active=True)
        return render(request, self.template_name, {
            'home_motivation':home_motivation,
            'blog_list':blog_list,
            'project_list':project_list,
            'service_list':service_list,
        })

class ServicesListView(ListView):
    template_name='services/index.html'

    def get(self, request):
        service_list = ServiceCategory.objects.all()
        return render(request, self.template_name, {
            'service_list':service_list,
        })
    
class BlogListView(ListView):
    template_name='blog/index.html'

    def get(self, request):
        blog_list = BlogCategory.objects.all()
        return render(request, self.template_name, {
            'blog_list':blog_list,
        })

class ProjectsListView(ListView):
    template_name='projects/index.html'

    def get(self, request):
        project_list = ProjectCategory.objects.all()
        return render(request, self.template_name, {
            'project_list':project_list,
        })
    
def smm(request):
    return render(request, 'services/smm/index.html')
    
def onlinestore(request):
    return render(request, 'services/online-store/index.html')
    
def website(request):
    return render(request, 'services/website/index.html')    

def servers(request):
    return render(request, 'blog/servers/index.html')
    
def whyuneedawebsite(request):
    return render(request, 'blog/why-u-need-a-website/index.html')
    
def seo(request):
    return render(request, 'blog/seo/index.html')
    
def brand(request):
    return render(request, 'blog/brand/index.html')


