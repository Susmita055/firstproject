
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post_list(request):
    return render(request,'post_list.html', {})

def home(request):
    return HttpResponse("HELLO!!!")

def index(request):
    return render(request, 'index.html', {})
