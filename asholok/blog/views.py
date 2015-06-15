from django.shortcuts import render
from django.core.urlresolvers import reverse 
from django.views import generic
from blog.models import Post, Comment, User
from my_auth.backends import PREPARED_BACKENDS
from form import PostForm
from django.http import HttpResponseRedirect

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
        context['comments'] = Comment.objects.filter(post_id=context['post'].id)
        # context['comments'] = Comment.objects.get()

        return context

class PostCreator(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/form.html'
    
    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(PostCreator, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('blog:index')

    def get_context_data(self, **kwargs):
        context = super(PostCreator, self).get_context_data(**kwargs)
        context['action'] = reverse('blog:form')
        context['available_backends'] = PREPARED_BACKENDS

        return context


    def form_valid(self, form):
        form.instance.author = User.objects.get(
                                user_mail=self.request.session['user_mail'])

        return super(PostCreator, self).form_valid(form)


# class CommentCreator(generic.CreateView):
#     model = Comment

#     def get_succsess_url(self):
#         return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

#     def form_valid(self, form):
#         form.instance.author = User.objects.get(
#                                 user_mail=self.request.session['user_mail'])
#         form.instance.post = Post.objects.get(
#                                 id=self.request.POST['post_id'])

#         return super(ComentCreator, self).form_valid(form)

def create_comment(request):
    if request.method == 'POST':
        comment = Comment(
            author=User.objects.get(user_mail=request.session['user_mail']),
            post=Post.objects.get(id=request.POST['post_id']),
            content=request.POST['comment'])
        comment.save()
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    return HttpResponseRedirect('/')

# Create your views here.
