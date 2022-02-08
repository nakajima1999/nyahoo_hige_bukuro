from django.urls import path

from blog.views import IndexView, PostDetailView, CatListView, FeatureListView,  PlaceListView, CatPostView, FeaturePostView, PlacePostView, SearchPostView, PostYearList, PostMonthList, YearPostView

app_name = 'blog'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('cats/', CatListView.as_view(), name='cat_list'),
    path('features/', FeatureListView.as_view(), name='feature_list'),
    path('places/', PlaceListView.as_view(), name='place_list'),
    path('cat/<str:cat_slug>/', CatPostView.as_view(), name='cat_post'),
    path('feature/<str:feature_slug>/', FeaturePostView.as_view(), name='feature_post'),
    path('place/<str:place_slug>/', PlacePostView.as_view(), name='place_post'),
    path('search/', SearchPostView.as_view(), name='search_post'),
    #path('post/<int:year>/', PostYearList.as_view(), name='year_post'),
    path('post/<int:year>/<int:month>/', PostMonthList.as_view(), name='month_post'),

    path('post/<int:year>/', YearPostView.as_view(), name='year_post'),
]

