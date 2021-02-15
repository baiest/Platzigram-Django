from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime

posts = [
    {
        'title': 'Mont Blac',
        'user': {
            'name': 'Juan Ballesteros',
            'picture': 'https://picsum.photos/60/60?image=958'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200?image=1036'
    },
    {
        'title': 'Via Lactea',
        'user': {
            'name': 'Camila Sanchez',
            'picture': 'https://picsum.photos/60/60?image=958'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200?image=415'
    },
    {
        'title': 'Auditorio',
        'user': {
            'name': 'Daniel Aristisaba',
            'picture': 'https://picsum.photos/60/60?image=958'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200?image=785'
    }
]

@login_required
def list_posts(request):
    profile = request.user.profile
    return render(request, 'posts/feed.html', 
    {'posts': posts, 
    'profile':profile,
    'user':request.user,})