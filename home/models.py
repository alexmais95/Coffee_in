from django.db import models
from django.urls import reverse


class Coffee(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')
    description = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Кавові напої'
        verbose_name_plural = 'Кавусік'
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорії кавусіка'
        ordering = ['id']
