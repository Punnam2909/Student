from django.db import models

# Create your models here.

class Sinfo(models.Model):
    Name=models.CharField(max_length=50)
    GPA=models.IntegerField()
    



    # update GPA 10
    # where GPA is 8









class Meta:
    verbose_name = "Sinfo"
    verbose_name_plural = "Sinfos"


def __str__(self):
    self.Name