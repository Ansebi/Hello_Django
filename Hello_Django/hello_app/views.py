from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

POSTS_PER_PAGE = 3

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
    paginate_by = POSTS_PER_PAGE


class AuthorPostListView(ListView):
    model = Post
    template_name = 'hello_app/author_posts.html'
    context_object_name = 'posts'
    paginate_by = POSTS_PER_PAGE

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


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


def global_():
    pass


global_.counter = 0


@staff_member_required
def charts(request):
    print(request)
    if request.GET.get('The_Button'):
        if request.GET.get('The_Button').isnumeric():
            global_.counter += 1
    else:
        global_.counter = 0
    return render(request, 'hello_app/charts.html',
                  {
                      'title': 'Charts',
                      'test_var': global_.counter
                  })
