from django.urls import path
from . import views
from .views import AboutCatListView

app_name = 'about'
urlpatterns = [
    path('', AboutCatListView.as_view()),
]
