from django.urls import path
from newsline.views import NewsListView

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
]

