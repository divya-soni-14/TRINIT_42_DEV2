from django import forms
from .models import bugs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


STATUS_OPTIONS = [("0", 0), ("1", 1), ("2", 2), ("3", 3), ("4", 4)]


class BugForm(forms.ModelForm):
    class Meta:
        model = bugs
        fields = ("title", "bug", "tags")

    # def __init__(self, *args, **kargs):
    #     super().__init__(*args, **kargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = "post"
    #     self.help.add_input(Submit)


<<<<<<< HEAD
class UserCreateForm(UserCreationForm):
    class Meta:
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )
        model = User
=======
class AssignForm(forms.ModelForm):
    class Meta:
        model = bugs
        fields = ("status", "visibility", "is_public", "deadline", "assignee")
>>>>>>> e445bc17700e5eb638488fc925f47e7a0ff02db9
