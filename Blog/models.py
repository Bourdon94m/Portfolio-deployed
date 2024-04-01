from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Category Name", unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name="Author Name", unique=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    date = models.DateField(auto_now=True)
    description = models.CharField(max_length=255, blank=False, null=False)
    body = RichTextField(blank=False, null=False, verbose_name="Content of the blog")
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)