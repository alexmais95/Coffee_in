from django.db import models


class Coffee(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField()
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
