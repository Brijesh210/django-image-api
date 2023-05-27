from django.db import models
from django.contrib.auth.models import AbstractUser


class SizedTier(models.Model):
    size = models.IntegerField()

    def __str__(self) -> str:
        return str(self.size)


class Tier(models.Model):
    tier_name = models.CharField(max_length=50, null=True)

    sizes = models.ManyToManyField(SizedTier, related_name="tier_user", null=True)
    orignal_image = models.BooleanField(default=False)
    expire_link = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.tier_name


class User(AbstractUser, models.Model):
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE, related_name="user_tier", null=True)


class SizedImage(models.Model):
    size = models.IntegerField()

    def __str__(self) -> str:
        return str(self.size)


class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_image", null=True, blank=True)
    sizedImages = models.ManyToManyField(SizedImage, related_name="sizedimage_image", null=True, blank=True)
