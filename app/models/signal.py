from enum import Enum

from django.db import models


class QuartierEnum(Enum):
    QUARTIER_1 = '1'
    QUARTIER_2 = '2'
    QUARTIER_3 = '3'
    QUARTIER_4 = '4'
    QUARTIER_5 = '5'
    QUARTIER_6 = '6'
    QUARTIER_7 = '7'
    QUARTIER_8 = '8'
    QUARTIER_9 = '9'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class Signal(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    quartier = models.CharField(
        max_length=200,
        choices=QuartierEnum.choices()
    )