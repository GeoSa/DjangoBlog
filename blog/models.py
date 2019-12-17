from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    category_title = models.CharField('Заголовок', max_length=50)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_title


class Tag(models.Model):
    tag_title = models.CharField('Тег', max_length=50)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.tag_title


class News(models.Model):
    news_author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE)
    news_category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL, null=True)
    news_title = models.CharField('Заголовок', max_length=150)
    news_preview = models.TextField('Аннотация', max_length=350)
    news_text = models.TextField('Текст')
    news_tag = models.ManyToManyField(Tag, verbose_name='Теги')
    created_date = models.DateTimeField('Дата', auto_now_add=True)
    news_description = models.CharField('Описание', max_length=100)
    news_keywords = models.CharField('Ключевые слова', max_length=50)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.news_title


class Comment(models.Model):

    comment_user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE
    )
    comment_news = models.ForeignKey(
        News,
        verbose_name="Новость",
        on_delete=models.CASCADE,
    )
    comment_text = models.TextField()

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return "{}".format(self.comment_user)

