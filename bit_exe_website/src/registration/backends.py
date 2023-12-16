# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model
# from djongo import database

# class MongoDBBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         UserModel = get_user_model()
#         try:
#             # Try to find a user matching your username
#             user = UserModel.objects.get(username=username)
#             #  Check the password is the one we have for the user
#             if user.check_password(password):
#                 return user
#         except UserModel.DoesNotExist:
#             # Run the default password hasher once to reduce the timing
#             # difference between an existing and a non-existing user.
#             UserModel().set_password(password)

#     def get_user(self, user_id):
#         UserModel = get_user_model()
#         try:
#             return UserModel.objects.get(pk=user_id)
#         except UserModel.DoesNotExist:
#             return None