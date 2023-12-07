# from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator



#previous running code - start
from djongo import models
from django.contrib.auth.models import User

# Create your models here.
class TaskListItems(models.Model):
    content = models.TextField()
class TaskAssigned(models.Model):
    user_profile = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey(TaskListItems,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user_profile.username}'s Task: {self.task.content}"
#previous running code - end    




    # username = models.CharField(max_length=25)
    # email = models.EmailField(max_length=100)
    # password = models.CharField(
    #     max_length=25,
    #     validators=[
    #         MinLengthValidator(8, message='Password must have a minimum length of 8 characters.'),
    #         MaxLengthValidator(25, message='Password must have a maximum length of 25 characters.')
    #     ]
    # )
# class users(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username



# from djongo import models
# from django.contrib.auth.models import AbstractUser,Group,Permission
# from django.utils.translation import gettext_lazy as _

# class CustomUser(AbstractUser):
#     username = models.TextField(unique=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=25,
#         validators=[
#             MinLengthValidator(8, message='Password must have a minimum length of 8 characters.'),
#             MaxLengthValidator(25, message='Password must have a maximum length of 25 characters.')
#         ]
#     )
   

# class TaskListItems(models.Model):
#     user_profile = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     content = models.TextField()
#     # Add other task-related fields

# class TaskAssigned(models.Model):
#     user_profile = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
#     task = models.ForeignKey(TaskListItems,on_delete=models.CASCADE)
#     def __str__(self):
#         return f"{self.user_profile.username}'s Task: {self.task.content}"
    
# class Meta:
#         # Define unique related names for user's groups and permissions
#         # Adjust these names to avoid conflicts with the default user model
#         # Choose meaningful and unique names
#         groups = models.ManyToManyField(
#             Group,
#             verbose_name=_('groups'),
#             blank=True,
#             related_name='custom_user_group',  # Unique related name for groups
#             related_query_name='custom_user_group',
#         )
#         user_permissions = models.ManyToManyField(
#             Permission,
#             verbose_name=_('user permissions'),
#             blank=True,
#             related_name='custom_user_permission',  # Unique related name for permissions
#             related_query_name='custom_user_permission',
#         )