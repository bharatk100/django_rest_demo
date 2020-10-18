from django.db import models


class employee(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)

    def __str__(self):
        return self.firstname