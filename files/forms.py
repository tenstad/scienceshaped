from django import forms

class ImageUpload(forms.Form):
    title = forms.CharField(max_length=100)
    file = forms.FileField()