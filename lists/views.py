from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(requests):
    return HttpResponse('<html><title>To-Do lists</title></html>')
