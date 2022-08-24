from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Snack(models.Model):
    name = models.CharField(max_length=128)
    # primary key in another table, in this case Django's get_user_model
    # on_delete=models.CASCADE deletes everything the user created
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default=' ')
    # integer_example = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}:    {self.description}'




