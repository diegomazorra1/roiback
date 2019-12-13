from django.db import models
from django_userforeignkey.models.fields import UserForeignKey
# Create your models here.


class Base(models.Model):
    estado = models.BooleanField(default=True)
    datecreated = models.DateTimeField(auto_now_add=True)
    datemodif = models.DateTimeField(auto_now=True)
    # uc = models.ForeignKey(User, on_delete=models.CASCADE)
    # um = models.IntegerField(blank=True,null=True)
    uscreate = UserForeignKey(auto_user_add=True,related_name='+')
    usmodificate = UserForeignKey(auto_user=True,related_name='+')

    class Meta:
        abstract=True
