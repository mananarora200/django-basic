from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.conf import settings
import os
# Create your views here.
from . import forms
from django.core.paginator import Paginator


def home(request):
    user_list = models.Image_Model.objects.all().order_by("-id")
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 8)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, "home.html", { 'users': users ,'media_url':settings.MEDIA_URL})

def image_upload(request):
    return render(request, "image_upload.html") 

def Upload(request):
    tag_list = request.POST.getlist("tags")
    tags = ""
    for i in tag_list:
        tags+=i+" "
    count_obj = models.Image_Model.objects.last()
    try:
        count = count_obj.id
    except:
        count = 0
    for i, x in enumerate(request.FILES.getlist("files")):
        count1 = i + count
        def process(f):
            count_obj = models.Image_Model.objects.last()
            
            with open(os.getcwd()+'\\media\\images\\file_' + str(count1) + ".jpg", 'wb+') as destination:
                for chunk in f.chunks():
                    image_instance = models.Image_Model.objects.create(tags=tags,upload_image=os.getcwd()+'\\media\\images\\file_' + str(count1) + ".jpg")
                    destination.write(chunk)
        process(x)
    return home(request)

def search_by_tag(request):
    tag = request.POST.get("tag")
    print(tag)
    user_list = models.Image_Model.objects.filter(tags__contains=tag).order_by("-id")
    print(user_list)
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 8)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, "home.html", { 'users': users ,'media_url':settings.MEDIA_URL})

def view_image(request,pk):
    user=models.Image_Model.objects.filter(id=pk)
    return render(request,"view.html",{'users':user,'media_url':settings.MEDIA_URL})
    