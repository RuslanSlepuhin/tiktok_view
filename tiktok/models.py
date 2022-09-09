from django.db import models

# Create your models here.
class Auth(models.Model):
    field = models.JSONField()

    def __str__(self):
        return self.field[0:50]


class CallBack(models.Model):
    field = models.CharField(max_length=4000)

    def __str__(self):
        return self.field[0:50]

