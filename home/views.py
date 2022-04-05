from django.shortcuts import render
from .models import Footer, SocialMedia

# Create your views here.


def index(request):

    """
    A view to return the index page
    """
    footer = Footer.objects.all()
    social_media = SocialMedia.objects.all()

    context = {

        'footer': footer,
        'social_media': social_media
    }
    return render(request, 'home/index.html', context)
