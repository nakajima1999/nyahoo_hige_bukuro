from django.db.models import Count, Q

from blog.models import Cat, Feature, Place


def common(request):
    context = {
        'cats': Cat.objects.annotate(
            num_posts=Count('post', filter=Q(post__is_public=True))),
        'features': Feature.objects.annotate(
            num_posts=Count('post', filter=Q(post__is_public=True))),
        'places': Place.objects.annotate(
            num_posts=Count('post', filter=Q(post__is_public=True))),
    }
    return context