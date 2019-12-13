from django.db import models
from django.contrib.auth.models import User
import datetime
import time
from django.utils import timezone
from apps.bases.models import Base


# Create your models here.








class RegisterHotel(models.Model):

    name= models.CharField(max_length=50)
    image = models.ImageField(upload_to='profiles', null=True, blank=True)
    description= models.CharField(max_length=82)
    locationchoice=(('Medellin','Medellin'),('Bogota','Bogota'),('Neiva','Neiva'))
    location=models.CharField(choices=locationchoice,default="Medellin",max_length=8)
    #created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    #updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    like = models.ManyToManyField(User,related_name="users_interested", blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events", blank=True, null=True)
    unlike = models.ManyToManyField(User,related_name="users_not_interested", blank=True)
    signed_up = models.ManyToManyField(User,related_name="users_reservers", blank=True)

    def __str__(self):
        return '{} '.format(self.id)

#    def save(self,*args, **kwargs):
    #    self.created_by=user.get_id
    #    return super(Transaccion, self).save( *args, **kwargs)




class Categoria(Base):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Categoría',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural= "Categorias"



class Comment(models.Model):
    post = models.ForeignKey(RegisterHotel, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="eventsc")
    approved_comment = models.BooleanField(default=True)
