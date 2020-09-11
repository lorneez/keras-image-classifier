from django import forms

class ImageForm(forms.Form):
    class Meta:
        image = forms.FileField()
