from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, models.CASCADE, 'blog')
    tags = models.ManyToManyField(Tag, 'blog')
    image = models.ImageField(upload_to='blog')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
