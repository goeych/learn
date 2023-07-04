from django.shortcuts import render
from django.core.signals import request_finished
from django.dispatch import receiver
from django.http import HttpResponse
from .models import Post
from django.db.models.signals import post_save,pre_save

# Create your views here.

def home(request):
    p10 = Post.objects.create(title="p10 title")              
    return HttpResponse("here the response")

@receiver(pre_save, sender=Post)
def save_pre(sender,**kwargs):
    print("web pre-save")

@receiver(post_save,sender=Post)
def save_post(sender, **kwargs):
    print("web post save")

@receiver(request_finished)
def request_post(sender,**kwargs):
    print("request finished")


