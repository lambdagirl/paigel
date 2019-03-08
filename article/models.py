from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
import os
from django.template.defaultfilters import slugify
from django.shortcuts import get_object_or_404
  
class ArticleManager(models.Manager):
    use_for_related_fields = True

    def active(self, *args, **kwargs):
        return super(ArticleManager, self).filter(draft=False).filter(pub_date__lte=timezone.now())
'''
    def images(self, slug):
        article = None
        article= get_object_or_404(Article,slug=slug)
        images = Images.objects.filter(article__in=[article])
        return images
'''
def upload_location(instance, filename):
    PostModel = instance.__class__
    title = instance.article.title
    slug = slugify(title)
    return os.path.join( "article_images/%s-%s" % (slug, filename))


class Article(models.Model):
    title = models.CharField(max_length = 255, verbose_name= "Title")
    slug= models.SlugField(unique=True)
    body = models.TextField( verbose_name= "body")
    modified = models.DateTimeField(auto_now = True)
    draft = models.BooleanField(default=False)
    pub_date = models.DateField(auto_now=False, auto_now_add=False, blank=True,null=True)
    objects = ArticleManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-pub_date", "-modified"]

class Images(models.Model):
    article = models.ForeignKey(Article, default=None, on_delete = models.CASCADE)
    image = models.ImageField(upload_to=upload_location,
            null=True,
            blank=True)
