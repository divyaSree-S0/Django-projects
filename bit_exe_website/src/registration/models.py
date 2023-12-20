# from django.db import models
from djongo import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone
# from djongo.models.fields import ObjectId

# Create your models here.
class Users(models.Model):
    _id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    industry_name = models.CharField(max_length=100)
    mine_location = models.CharField(max_length=100)
    collection_name = models.CharField(max_length=100)
    last_login = models.DateTimeField(default=timezone.now)
    # conveyors = models.ArrayField(model_container=models.CharField,max_length=100)
    noConveyorSystem = models.IntegerField()
    class Meta:
        db_table = 'Users'
        app_label = 'mongodb'
    def __str__(self):
        return self.username
    # def save(self, *args, **kwargs):
    #     if self.pk is None:  # This is a new user
    #         self.passw = make_password(self.passw)
    #     else:  # This is an existing user
    #         orig = Users.objects.get(pk=self.pk)
    #         if orig.passw != self.passw:  # The password has been changed
    #             self.passw = make_password(self.passw)
    #     super().save(*args, **kwargs)
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

class Conveyors(models.Model):
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    # userId = models.CharField(max_length=150)
    name = models.CharField(max_length=100)
    totalPulleys = models.IntegerField()
    pulleysInShoe = models.IntegerField()
    beltThickness = models.IntegerField()
    beltWidth = models.IntegerField()
    beltLength = models.IntegerField()
    mine = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)

    class Meta:
        db_table =  'Conveyors'
        app_label = 'mongodb'

    # def create_collection(request,user):
    #     # user = Users.objects.get(username=request.session['username'])
    #     user._meta.db.create_collection(user.collection_name+"1")

