from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def has_review(self):
        return self.review_set.exists()


class UserFollows(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following'
    )
    followed_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followed_by'
    )

    class Meta:
        unique_together = ('user', 'followed_user', )


class Review(models.Model):
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    headline = models.CharField(max_length=128)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    body = models.TextField(max_length=8192, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
