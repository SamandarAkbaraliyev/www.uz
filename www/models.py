from django.db import models
from ckeditor.fields import RichTextField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=256)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Site(BaseModel):
    title = models.CharField(max_length=256)
    url = models.URLField(max_length=256)

    visitors = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    is_tas_ix = models.BooleanField(default=False)

    content = RichTextField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)


