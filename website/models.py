from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        template = '{0.name} {0.email} {0.message}'
        return template.format(self)   