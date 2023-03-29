from django.shortcuts import render
from django.views.generic import ListView
from .models import HomeMotivation, Project, Blog, Service

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