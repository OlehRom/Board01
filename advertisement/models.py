from django.db import models
from django.conf import settings
from django.utils import timezone


class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст оголошення')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Task, on_delete = models.CASCADE)
    author_name = models.CharField("ім'я автора", max_length = 50)
    comment_text = models.CharField('текст коменту', max_length = 200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарії'
