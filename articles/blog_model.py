from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):
    slug = models.SlugField(unique=True, max_length=200, verbose_name="Slug", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan Sana")
    meta_description = models.TextField(verbose_name="SEO Ta'rifi", blank=True, null=True)



    class Meta:
        abstract = True


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.__str__())
        super().save(*args, **kwargs)
