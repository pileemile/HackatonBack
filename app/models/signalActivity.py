from django.db import models


class SignalActivity (models.Model):
    id = models.AutoField(primary_key=True)
    signal = models.ForeignKey('Signal', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=200)
