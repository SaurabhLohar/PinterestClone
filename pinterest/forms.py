from django import forms
from .models import ImageFile,Comment


class UploadImage(forms.ModelForm):
	title = forms.CharField(required=True)
	 
	class Meta:
		model = ImageFile
		fields = ['title','about','image']


class CommentForm(forms.ModelForm):
    comment =forms.CharField(max_length=255)

    class Meta:
    	model = Comment
    	fields = ['comment']


