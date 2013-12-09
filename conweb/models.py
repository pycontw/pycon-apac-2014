from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField("auth.User")
    date_of_birth = models.DateField()
    brief = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
