from django.db import models


class PropActivity (models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

