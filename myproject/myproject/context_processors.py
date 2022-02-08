from django.db.models import Count, Q
from django.utils import timezone
from django.db.models.functions import TruncMonth

from blog.models import Cat, Feature, Place, Post


def common(request):
    context = {
        'cats': Cat.objects.annotate(
            num_posts=Count('post', filter=Q(post__is_public=True))),
        'features': Feature.objects.annotate(
            num_posts=Count('post', filter=Q(post__is_public=True))),
        'places': Place.objects.annotate(
            num_posts=Count('post', filter=Q(post__is_public=True))),
        #'dates': Post.objects.annotate(month=TruncMonth('discovery_date')).values('month').annotate(count=Count('pk'))

        'dates': Post.objects.dates('discovery_date', 'month', order='DESC'),
    
    }
    return context