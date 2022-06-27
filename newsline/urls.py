from django.urls import path
from newsline.views import NewsListView, AddNews

urlpatterns = [
    path('newsline/', NewsListView.as_view(), name='news_list'),
    path('add-news/', AddNews.as_view(), name='add_news'),
]

