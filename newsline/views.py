from django.views.generic import ListView

from newsline.models import News


class NewsListView(ListView):
    model = News
    template_name = 'newsline/index.html'
    context_object_name = 'news'

    def get_queryset(self):
        count = self.request.GET.get('count')
        queryset = self.queryset
        if count:
            queryset = queryset[:count]
        return queryset

