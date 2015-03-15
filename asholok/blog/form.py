from django.forms import ModelForm
from blog.models import Post

class PostForm(ModelForm):
	class Meta:
		model = Post
		exclude = ['author', 'slug', 'date']
