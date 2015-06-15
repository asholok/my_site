from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ['author', 'slug', 'date']
		widgets = {
			'body': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
		}
