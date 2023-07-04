from django.db import models
from django.db.models.signals import post_save,pre_save
from django.apps import AppConfig
from django.core.signals import setting_changed
from django.dispatch import receiver



class Post(models.Model):
    title= models.CharField(max_length=20)

    def __str__(self):
        return self.title
    
    #def my_callback(sender, **kwargs):
    #print("setting changed")


#def save_pre(sender,instance,**kwargs):
#    print("pre-save")
    
#pre_save.connect(save_pre,sender=Post)

#def save_post(sender,instance,**kwargs):
#    print("post_save")


#post_save.connect(save_post,sender=Post)
