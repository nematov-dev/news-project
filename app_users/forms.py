from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q


from app_users.models import UserProfileModel

UserModel = get_user_model()


class RegisterForm(UserCreationForm):
    
    image = forms.ImageField(required=False)

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username_or_email = forms.CharField(max_length=255)
    password = forms.CharField(max_length=128)

    def clean(self):
        username_or_email = self.cleaned_data["username_or_email"]
        password = self.cleaned_data["password"]

        try:
            user = UserModel.objects.get(
                Q(username=username_or_email) | Q(email=username_or_email)
            )
        except UserModel.DoesNotExist:
            raise forms.ValidationError("Username yoki Email xato")

        credentials = {"username": user.username, "password": password}
        authenticated_user = authenticate(**credentials)

        if authenticated_user is not None:
            self.cleaned_data["user"] = authenticated_user
            
        else:
            raise forms.ValidationError("Parolingiz xato")
        
        return self.cleaned_data


class UpdatePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name':'Ism',
            'last_name':'Familiya',
            'email':'Pochta'
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ['image']
        labels = {
            'image':'Rasm'
        }
        
