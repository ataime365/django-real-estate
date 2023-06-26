from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User

class CustomUserCreationForm(UserCreationForm):
    """Custom form for user creation"""
    class Meta(UserCreationForm):
        model = User
        fields = ["email","username", "first_name", "last_name"]
        error_class = "error"


class CustomUserChangeForm(UserChangeForm):
    """Custom form for user modification"""
    class Meta:
        model = User
        fields = ["email","username", "first_name", "last_name"]
        error_class = "error"