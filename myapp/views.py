from django.shortcuts import render
from django.http import HttpResponse



jobs = [
       { "title" : "Frontend Developer", 
         "company" : "Google", 
         "location" : "Remote", 
         "salary" : "$120k" 
       },
       { "title" : "Product Designer",
         "company" : "Figma", 
         "location" : "San Francisco, CA", 
         "salary" : "$135k" 
        }
        ]

# Create your views here.
def home(request):
    return render(request, "index.html", {"jobs":jobs})


def about(request):
    return HttpResponse("This is About Page")