from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import HomeBG, TourIdea, Comps
# Create your views here.


class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homebg = HomeBG.objects.all()
        tours = TourIdea.objects.all()
        comp = Comps.objects.all()
        return render(request, self.template_name, {'homebg':homebg, 'tours':tours, 'comp':comp})


class AboutListView(ListView):
    template_name = 'aboutus.html'

    def get(self, request):
        return render(request, self.template_name)