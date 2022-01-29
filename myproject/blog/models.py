from django.db import models
from django.utils import timezone

# 猫の名前
class Cat(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# ヒゲの特徴
class Feature(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# ヒゲの発見場所
class Place(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# 投稿
class Post(models.Model):
    title = models.CharField(max_length=255) ##
    cats = models.ManyToManyField(Cat)

    discovery_date = models.DateField(default=timezone.now)  # 発見日
    length = models.FloatField(blank=True, null=True, default=0)  # 長さ 

    features = models.ManyToManyField(Feature, blank=True)
    feature_description = models.TextField(blank=True)

    places = models.ManyToManyField(Place)  # ヒゲの発見場所: 複数可
    place_description = models.TextField(blank=True)  # その他のヒゲの発見場所の説明

    image = models.ImageField(upload_to='post_images/', null=True, blank=True) # 画像

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title