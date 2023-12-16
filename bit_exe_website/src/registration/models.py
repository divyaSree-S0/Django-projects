# from django.db import models
from djongo import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Users(models.Model):
    _id = models.IntegerField(primary_key=True)
    user = models.CharField(max_length=100,unique=True)
    passw = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    industry_name = models.CharField(max_length=100)
    mine_location = models.CharField(max_length=100)
    collection_name = models.CharField(max_length=100)
    class Meta:
        db_table = 'Users'
        app_label = 'mongodb'
    def __str__(self):
        return self.user
    # def save(self, *args, **kwargs):
    #     if self.pk is None:  # This is a new user
    #         self.passw = make_password(self.passw)
    #     else:  # This is an existing user
    #         orig = Users.objects.get(pk=self.pk)
    #         if orig.passw != self.passw:  # The password has been changed
    #             self.passw = make_password(self.passw)
    #     super().save(*args, **kwargs)
    def save(self, *args, **kwargs):
        self.passw = make_password(self.passw)
        super().save(*args, **kwargs)