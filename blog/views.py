from django.shortcuts import render
# Create your views here.
posts = [
    {
        'author': 'Abaidi Khaoula',
        'title': 'Blog TIC',
        'content': 'All TIC courses',
        'date_posted': 'January 15, 2020'
    },
{
        'author': 'Abaidi Khaoula',
        'title': 'Blog Programmation',
        'content': 'All Programmation courses',
        'date_posted': 'January 15, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})