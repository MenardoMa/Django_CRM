from django.db import models

# Create your models here.

#un model consiste a creer une table dans la base de donnéé
#Et chaque variable constitut une colonne dans la BD

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email      = models.CharField(max_length=50)
    phone      = models.CharField(max_length=15)
    adress     = models.CharField(max_length=100)
    city       = models.CharField(max_length=50)
    state      = models.CharField(max_length=50)
    zipcode    = models.CharField(max_length=20)

    def __str__(self):
        return (f"{self.first_name} {self.last_name} ")