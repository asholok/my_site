from django.shortcuts import render
from django.core.urlresolvers import reverse 
from django.views import generic
from blog.models import Post, User
from my_auth.backends import PREPARED_BACKENDS
# from my_auth.mixin import LoginRequiredMixin
from form import PostForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class Index(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = "posts_list"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['available_backends'] = PREPARED_BACKENDS

        return context

class Detail(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)
        context['available_backends'] = PREPARED_BACKENDS

        return context

class CreatePost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/form.html'
    
    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(CreatePost, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        if self.request.method == 'POST':
            try:
                print self.request.FILES
            except ValueError:
                print 'Do not pass img from form'
        return reverse('blog:index')

    def get_context_data(self, **kwargs):
        context = super(CreatePost, self).get_context_data(**kwargs)
        context['action'] = reverse('blog:form')

        #context['available_backends'] = PREPARED_BACKENDS

        return context


    def form_valid(self, form):
        form.instance.author = User.objects.get(user_mail=self.request.session['user_mail'])

        return super(CreatePost, self).form_valid(form)


# Create your views here.
