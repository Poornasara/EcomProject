from .models import Category

def Cat_links(request):
    links = Category.objects.all()
    return dict(links=links)