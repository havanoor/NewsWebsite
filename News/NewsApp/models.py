from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
# Create your models here.
class Choices(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    topics=(
        ('Business','Business'),
        ('Sports','Sports'),
        ('Technology','Technology'),
        ('Entertainment','Entertainment'),

    )
    preferences=MultiSelectField(choices=topics)

    # def __str__(self):
    #     return self.preferences