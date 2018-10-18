from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class category (models.Model):
    name= models.CharField(max_length=100,verbose_name ="Nombre")
    created= models.DateTimeField(auto_now_add=True,verbose_name ="Fecha creacion")
    update= models.DateTimeField(auto_now=True,verbose_name ="fecha edicion")

    class Meta:
        verbose_name ="categoria"
        verbose_name_plural="categorias"
        ordering =['-created']
    def __str__(self):
        return self.name

class post(models.Model):
    title =models.CharField(max_length=200,verbose_name ="titulo")
    content= models.TextField(verbose_name ="Contenido")
    published = models.DateTimeField(verbose_name ="fecha de publicacion",default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog",null=True,blank=True)
    author =models.ForeignKey(User,verbose_name="autor",on_delete=models.CASCADE)
    cotegories = models.ManyToManyField(category,verbose_name="categorias",related_name="get_posts")
    created= models.DateTimeField(auto_now_add=True,verbose_name ="Fecha creacion")
    update= models.DateTimeField(auto_now=True,verbose_name ="fecha edicion")

    class Meta:
        verbose_name ="entrada"
        verbose_name_plural="entradas"
        ordering =['-created']
    def __str__(self):
        return self.title