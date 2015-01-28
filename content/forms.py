from django import forms
from .models import Franchise, Feedback


class FranchiseForm(forms.ModelForm):
	name = forms.CharField(max_length=120)
	email = forms.EmailField()
	mobile = forms.CharField(max_length=12)
	address = forms.CharField(widget=forms.Textarea)
	city = forms.CharField(max_length=120)
	comments = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = Franchise


class FeedbackForm(forms.ModelForm):
	name = forms.CharField(max_length=120)
	email = forms.EmailField()
	subject = forms.CharField(max_length=120)
	message = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = Feedback		