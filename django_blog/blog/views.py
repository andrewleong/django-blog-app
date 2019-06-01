from django.shortcuts import render

mockPosts = [
    {
        'author': 'Andrew Leong',
        'title': 'My new macbook pro',
        'content': 'My first content',
        'date_posted': 'May 10, 2019'
    },
    {
        'author': 'Sarah Lee',
        'title': 'My new mac mini',
        'content': 'My second content',
        'date_posted': 'May 28, 2019'
    }
]

def home(request):
    # context is for passing data to templates
    context = {
        'posts': mockPosts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
