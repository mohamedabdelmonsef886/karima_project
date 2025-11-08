from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, verbose_name='الهاتف')
    address = models.TextField(blank=True, verbose_name='العنوان')

    def __str__(self):
        return self.user.username