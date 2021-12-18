from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser

class CustomUserCreationForms(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'username', 'age')

class CustomUserChangeForms(UserChangeForm):
    class Meta:
        model= CustomUser
        fields = ('first_name', 'last_name', 'email', 'username', 'age')