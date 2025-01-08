from django.db import models
from django.urls import reverse
from .blog_model import BaseModel


class Author(BaseModel):
    name = models.CharField(max_length=100, verbose_name="Muallif ismi")
    bio = models.TextField(verbose_name="Biografiya")
    email = models.EmailField(unique=True, verbose_name="Email")

    def __str__(self):
        return self.name

    def get_detail_url(self):
        return reverse('blog_detail', args=[
            self.name.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])


class Article(BaseModel):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    content = models.TextField(verbose_name="Maqola matni")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="articles", verbose_name="Muallif")
    image = models.ImageField(upload_to="articles/images/", verbose_name="Rasm", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_detail_url(self):
        return reverse('article_detail', args=[
            self.author.slug,
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])
