from django.db import models

# Create your models here.
class details(models.Model):
    sid = models.IntegerField()
    sname = models.CharField(max_length=60)
    class Meta:
        db_table = "Student details"
