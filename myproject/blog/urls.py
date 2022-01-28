# blog/urls.py

from django.urls import path

from blog.views import IndexView, PostDetailView, CatListView, FeatureListView, CatPostView, FeaturePostView

app_name = 'blog'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('cats/', CatListView.as_view(), name='cat_list'),
    path('features/', FeatureListView.as_view(), name='feature_list'),
    path('cat/<str:cat_slug>/', CatPostView.as_view(), name='cat_post'),
    path('feature/<str:feature_slug>/', FeaturePostView.as_view(), name='feature_post'),
]

