from django.shortcuts import render
from .models import blogTable

def home(request):
    database = blogTable.objects.all()
    return render(request,"blog.html",{"database" : database})

def content(req,pk):
    database = blogTable.objects.get(id = pk)
    return render(req,'content.html',{"db":database})