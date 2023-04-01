from django.shortcuts import render, redirect
from .models import Contacts
from .forms import Contactus

# Create your views here.
def contactus(request):
    if request.method == 'POST':
        form = Contactus(request.POST)
        if form.is_valid():
            Contacts.objects.create(**form.cleaned_data)
            return redirect('contactus')
    else:
        form = Contactus()
    return render(request, 'contacts/index.html', context={'form':form})