from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>welcome</h1>")


def about(request):
    return HttpResponse("<h1>about the products</h1>")

def contact(request):
    return HttpResponse("<h1>contact</h1>")