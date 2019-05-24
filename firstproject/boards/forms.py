from django import forms
from .models import Topic



class NewTopicForm(forms.ModelForm):
	message = forms.CharField(widget=forms.Textarea(attrs={
		'rows':5,'placeholder':'What is the message'
		}), max_length=5000, help_text='The Max Lngth is 5000')
	class Meta:
		model = Topic
		fields = ['supject','message']
