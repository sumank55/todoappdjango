# from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# from django.contrib.auth.models import AbstractUser, UserManager
# from django.utils import timezone
# from django.conf import settings

# user = settings.AUTH_USER_MODEL

# class AccountUserManager(UserManager):
#     def _create_user(self, username, email, password,
#                      is_staff, is_superuser, **extra_fields):

#         now = timezone.now()
#         if not email:
#             raise ValueError('The given username must be set')

#         email = self.normalize_email(email)
#         user = self.model(username=email, email=email,
#                           is_staff=is_staff,
#                            is_active=True,
#                           is_superuser=is_superuser,
#                           date_joined=now, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

# class User(AbstractUser):
#     profile_image = models.ImageField('profile_image', upload_to='static/media', null=True, blank=True)
#     objects = AccountUserManager()

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=600,default=1)
    complete = models.BooleanField(default=False)
    create = models.DateField(auto_now=True)



    def __str__(self):
        return self.title

    class Meta:
        ordering=['complete']    

