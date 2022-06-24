from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name="заголовок")
    date = models.DateField(auto_now_add=True, verbose_name="дата публикации")
    text = models.TextField(verbose_name="ело новости")
    image = models.ImageField(verbose_name="картинка", null=True)

    def __str__(self):
        return self.title