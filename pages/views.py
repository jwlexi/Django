from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<title>ILoveWeVote</title><h1>Hello World, my name is Alexis Sanchez. This is my Django Project. </h1> <br> I'm building this project in preparation of an internship with a wonderful company called WeVote You can click here to find them at WeVote.us")
    