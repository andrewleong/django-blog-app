from django.shortcuts import render
# from django.http import HttpResponse

# Fake data
posts = [
    {
        'author': 'Andrew',
        'title': 'Blog post 1',
        'content': 'First content here',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Slaine',
        'title': 'Blog post 2',
        'content': 'Second content here',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
