from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class BaseModel(models.Model):
    short_text = models.CharField(max_length=100)
    long_text = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.short_text)
        super(BaseModel, self).save(*args, **kwargs)


class Author(BaseModel):
    email = models.EmailField(unique=True, verbose_name="Email")

    def __str__(self):
        return self.short_text


class Article(BaseModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="articles", verbose_name="Muallif")
    image = models.ImageField(upload_to="articles/images/", verbose_name="Rasm", blank=True, null=True)

    def __str__(self):
        return self.short_text

    def get_detail_url(self):
        return reverse('articles:article_detail', kwargs={
            'year': self.created_at.year,
            'month': self.created_at.month,
            'day': self.created_at.day,
            'slug': self.slug
        })

class Comment(BaseModel):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comment_set')
    email = models.EmailField()

    def __str__(self):
        return self.short_text
