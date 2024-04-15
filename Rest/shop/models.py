from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField
import uuid 
import os
from datetime import datetime
User = get_user_model()
# Create your models here.



class Shared(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        abstract = True


    
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)
# from sorl.thumbnail import ImageField, get_thumbnail
def get_covert_path(obj, fn):
    ex = os.path.splitext(fn)[1]
    uid = uuid.uuid5(uuid.NAMESPACE_URL,f"store-book-{obj.pk}" )
    path =datetime.now().strftime(f"book_covers/%Y/%m/%d/{uid}{ex}")
    return path

class Product(Shared):
    TOPIC_CHOICES = (
            ("availble", "availble"),
            ("Finished", "Finished"),
        )
    CHOICES = (
            ("sprts", "sports"),
            ("inf", "inf"),
        )
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_seller')
    color = models.CharField(max_length=255)
    description = models.TextField(max_length=300)
    imgs = models.FileField(upload_to=get_covert_path, blank=True, null=True)
    status = models.CharField(choices=TOPIC_CHOICES, max_length=100)
    category = models.CharField(choices=CHOICES, max_length=100)
    def __str__(self):
        return self.name




class Comment(Shared):
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    parent = models.ForeignKey('Comment', related_name='replies', on_delete=models.PROTECT, null=True, blank=True)