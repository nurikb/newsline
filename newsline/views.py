from django.views.generic import ListView, CreateView

from newsline.models import News
from newsline.forms import NewsForm


class AddNews(CreateView):
    model = News
    template_name = 'newsline/add_news.html'
    form_class = NewsForm
    success_url = '/newsline'


class NewsListView(ListView):
    model = News
    template_name = 'newsline/index.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        count = self.request.GET.get('count')
        queryset = self.object_list
        print(count)
        if count:
            queryset = queryset[:int(count)]
        return {'news': queryset}

