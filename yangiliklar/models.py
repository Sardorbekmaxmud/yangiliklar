from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('a','admin'),
        ('u','user')
    )

    roles = models.CharField(max_length=1,choices=ROLE_CHOICES)

class CategoryModel(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None,null=True)
    name = models.CharField(max_length=65,default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'

class NewModel(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None,null=True)
    category = models.ForeignKey(CategoryModel,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=250,default='')
    text = models.TextField(default='')
    create_at = models.DateTimeField(default=datetime.now)
    update_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'new'
