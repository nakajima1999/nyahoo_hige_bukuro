from django.db.models import Count, Q
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views import generic
from django.shortcuts import get_object_or_404

from blog.models import Post, Cat, Feature, Place


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.is_public and not self.request.user.is_authenticated:
            raise Http404
        return obj


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 6


class CatListView(ListView):
    queryset = Cat.objects.annotate(
        num_posts=Count('post', filter=Q(post__is_public=True)))


class FeatureListView(ListView):
    queryset = Feature.objects.annotate(num_posts=Count(
        'post', filter=Q(post__is_public=True)))

class PlaceListView(ListView):
    queryset = Place.objects.annotate(num_posts=Count(
        'post', filter=Q(post__is_public=True)))


class CatPostView(ListView):
    model = Post
    template_name = 'blog/cat_post.html'

    def get_queryset(self):
        cat_slug = self.kwargs['cat_slug']
        self.cat = get_object_or_404(Cat, slug=cat_slug)
        qs = super().get_queryset().filter(cats=self.cat)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat'] = self.cat
        return context


class FeaturePostView(ListView):
    model = Post
    template_name = 'blog/feature_post.html'

    def get_queryset(self):
        feature_slug = self.kwargs['feature_slug']
        self.feature = get_object_or_404(Feature, slug=feature_slug)
        qs = super().get_queryset().filter(features=self.feature)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feature'] = self.feature
        return context

class PlacePostView(ListView):
    model = Post
    template_name = 'blog/place_post.html'

    def get_queryset(self):
        place_slug = self.kwargs['place_slug']
        self.place = get_object_or_404(Place, slug=place_slug)
        qs = super().get_queryset().filter(places=self.place)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['place'] = self.place
        return context

class SearchPostView(ListView):
    model = Post
    template_name = 'blog/search_post.html'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        lookups = (
            Q(title__icontains=query) |
            Q(cats__name__icontains=query) |
            Q(features__name__icontains=query) |
            Q(places__name__icontains=query)
        )

        if query is not None:
            qs = super().get_queryset().filter(lookups).distinct()
            return qs
        qs = super().get_queryset()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context


class ArchiveListMixin:
    model = Post
    paginate_by = 12
    date_field = 'created_at'
    template_name = 'blog/post_list.html'
    allow_empty = True
    make_object_list = True



class PostYearList(ArchiveListMixin, generic.YearArchiveView):

    def get_queryset(self):
        return super().get_queryset().select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = '{}年の日記'.format(self.kwargs['year'])
        return context


class YearPostView(ListView):
    model = Post
    template_name = 'blog/year_post.html'

    def get_queryset(self):
        year_slug = self.kwargs['place_slug']
        self.place = get_object_or_404(Place, slug=year_slug)
        qs = super().get_queryset().filter(years=self.place)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = self.place
        return context


class PostMonthList(ArchiveListMixin, generic.MonthArchiveView):
    month_format = '%m'

    def get_queryset(self):
        return super().get_queryset().select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = '{}年{}月の日記'.format(self.kwargs['year'], self.kwargs['month'])
        return context