from django.db import models

# Create your models here.

class Usuario(models.Model):
    name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Pescaria(models.Model):
    #key = models.IntegerField(default=0)
    local = models.CharField(max_length=200)
    date_time = models.DateTimeField('date published')
    members = models.ManyToManyField(
        Usuario,
        #through='Peixe',
        #through_fields=('user', 'origin'),
    )
    def __str__(self):
        return self.local
   


class Peixe(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    origin = models.ForeignKey(Pescaria, on_delete=models.CASCADE)
    size = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
