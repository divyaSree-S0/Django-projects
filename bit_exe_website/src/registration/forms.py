from django import forms

class LoginForm(forms.Form):
    # username = forms.TextInput()
    username = forms.CharField(max_length=100,required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100,required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(),required=True)
    email = forms.EmailField(required=True)
    industry_name = forms.CharField(max_length=100,required=True)
    mine_location = forms.CharField(max_length=100,required=True)

# class AuthenticatedForm(forms.Form):
#     username = forms.CharField(max_length=100, required=True)
#     password = forms.CharField(widget=forms.PasswordInput(), required=True)
#     pwd = None

#     def get_password_from_mongo(self):
#         # Assuming you have a MongoDB connection and collection set up
#         # Replace 'your_collection' with the actual name of your collection
#         collection = BIT_exe.Users

#         # Retrieve the password from the collection based on the username
#         document = collection.find_one({'username': self.cleaned_data['username']})
#         if document:
#             self.pwd = document['password']
#         else:
#             self.pwd = None
    
