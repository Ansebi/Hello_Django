from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 11, 2022'
    },
    {
        'author': 'Author 2',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 12, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'hello_app/home.html', context)


def about(request):
    return render(request, 'hello_app/about.html', {'title': 'An About Page'})
