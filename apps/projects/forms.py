from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "due_date"]
        widgets = {
            "due_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control"
                }
            ),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }