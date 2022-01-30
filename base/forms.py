from django import forms
from .models import bugs

STATUS_OPTIONS = [("0", 0), ("1", 1), ("2", 2), ("3", 3), ("4", 4)]


class BugForm(forms.ModelForm):
    class Meta:
        model = bugs
        fields = ("title", "bug", "tags")
