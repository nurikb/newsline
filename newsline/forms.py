from django.forms import ModelForm

from newsline.models import News


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = '__all__'
