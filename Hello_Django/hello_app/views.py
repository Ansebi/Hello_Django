from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'October 11, 2022'
#     },
#     {
#         'author': 'Author 2',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'October 12, 2022'
#     }
# ]


class PostListView(ListView):
    model = Post
    template_name = 'hello_app/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'title',
        'content'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView):

    model = Post
    fields = [
        'title',
        'content'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView):

    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'hello_app/home.html', context)


def about(request):
    return render(request, 'hello_app/about.html', {'title': 'An About Page'})
