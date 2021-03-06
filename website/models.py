from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100,blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(max_length=500,blank=False)
    def __str__(self):
        template = '{0.name} {0.email} {0.message}'
        return template.format(self)   

class Post(models.Model):
    name = models.CharField(max_length=300)
    desc = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    img = models.CharField(max_length=500)
    details = models.CharField(max_length=500)
    detailsTitle = models.CharField(max_length=500)

    def __str__(self):
        template = '{0.name} {0.desc} {0.price} {0.img}'
        return template.format(self)

class Equipo(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300)
    img = models.CharField(max_length=500)
    

    def __str__(self):
        template = '{0.title} {0.subtitle} {0.img}'
        return template.format(self)

class Inmuebles(models.Model):
    name = models.CharField(max_length=300)
    desc = models.CharField(max_length=300)
    tipo = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    img = models.CharField(max_length=500)
    details = models.CharField(max_length=500)
    detailsTitle = models.CharField(max_length=500)

    def __str__(self):
        template = '{0.name} {0.desc} {0.tipo} {0.price} {0.img}'
        return template.format(self)
     