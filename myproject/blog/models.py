from django.db import models
from django import forms
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
    title = models.CharField(max_length=255, verbose_name='タイトル') # タイトル
    cats = models.ManyToManyField(Cat, verbose_name='猫様（複数可）')  # 猫様：複数可

    discovery_date = models.DateField(default=timezone.now, verbose_name='発見日')  # 発見日
    length = models.FloatField(blank=True, null=True, default=0, verbose_name='ヒゲの長さ')  # 長さ 

    features = models.ManyToManyField(Feature, blank=True, verbose_name='ヒゲの特徴（複数可）')  # 特徴：複数可
    feature_description = models.TextField(blank=True, verbose_name='その他のヒゲの特徴')  # その他のヒゲの特徴の説明

    places = models.ManyToManyField(Place, verbose_name='発見場所（複数可）')  # ヒゲの発見場所: 複数可
    place_description = models.TextField(blank=True, verbose_name='その他の発見場所の特徴')  # その他のヒゲの発見場所の説明

    image = models.ImageField(upload_to='post_images/', null=True, blank=True, verbose_name='ヒゲの写真') # 画像

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日')  # 作成日
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日')  # 更新日
    published_at = models.DateTimeField(blank=True, null=True, verbose_name='公開日')  # 公開日
    is_public = models.BooleanField(default=False, verbose_name='公開する')  # 公開状況

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title