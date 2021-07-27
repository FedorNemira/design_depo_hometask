
from taggit.managers import TaggableManager
from django.db import models
from datetime import date
from PIL import Image
import uuid
import os


def get_photo_path(instance, filename):
    today = date.today()
    ext = filename.split(".")[-1].lower()
    if ext == "":
        ext = "jpg"
    if not ext:
        ext = "jpg"
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join("profile/", str(today.year), str(today.month), str(today.day), filename)


class Article(models.Model):
    name = models.CharField("Name", max_length=500, null=True, blank=True)
    category = models.CharField("Category", max_length=50, null=True, blank=True)
    photo = models.ImageField("Photo", upload_to=get_photo_path, null=True, blank=True)
    text = models.TextField("Text", max_length=50000, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    def __str__(self):
        return self.name


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField("Author", max_length=40)
    text = models.TextField("Text", max_length=1700, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        comment_date = self.creation_date.strftime('%d/%m/%y %H:%M')
        return f"{comment_date} : {self.article} : {self.author}"

    class Meta:
        ordering = ('-creation_date',)