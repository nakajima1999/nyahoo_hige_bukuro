from django.db import models
from django.utils import timezone

class AboutCat(models.Model):
    class Meta:
        db_table = 'cat'

    GENDER_CHOICES = (
        (1, 'オス'),
        (2, 'メス')
    )


    name = models.CharField(verbose_name='名前', max_length=255)  # 名前
    name_en = models.CharField(verbose_name='名前(英語)', max_length=255, default="")  # 名前(英語)
    born = models.CharField(verbose_name='生まれた年', max_length=50)  # 生まれた年月（不明の場合は予想）
    sex = models.IntegerField(verbose_name='性別', choices=GENDER_CHOICES, default=1)  # 性別
    character = models.TextField(verbose_name='性格', max_length=1000)  # 性格
    point = models.TextField(verbose_name='推しポイント', max_length=1000)  # 推しポイント（ココがかわいい）
    image = models.ImageField(upload_to='cat_images/', null=True, blank=True) # 画像

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        ret = str(self.name)
        return ret
