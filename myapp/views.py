from django.shortcuts import render
from django.http import HttpResponse
from .models import Job



jobs = Job.objects.all()

# Create your views here.
def home(request):
    return render(request, "index.html", {"jobs":jobs})


def about(request):
    return HttpResponse("This is About Page")