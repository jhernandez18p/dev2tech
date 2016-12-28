import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):

    _USER = 1
    CLIENT = 2
    STAFF = 3
    ROLE_CHOICES = (
        (_USER, 'User'),
        (CLIENT, 'Client'),
        (STAFF, 'Staff'),
    )

    GENRE_CHOICE = (
        (1,('Man')),
        (2,('Moman')),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=200, blank=True)
    genre = models.IntegerField(choices=GENRE_CHOICE,default=1)
    # account = models.ForeignKey(Account,on_delete=models.CASCADE, )
    avatar = models.ImageField(upload_to="user/avatar/",blank=True)
    created = models.DateTimeField(auto_now=True,auto_now_add=False)
    time_stamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    location = models.CharField(max_length=30, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    def user_name(self):
        return '%s %s' % (self.user.first_name, self.user.last_name,)

    def __str__(self):
        return self.user_name()

    class Meta:

        verbose_name = ('User Profile')
        verbose_name_plural = ('User Profile')
        permissions = (
            ("can_create_user", "Can create user"),
            ("can_delete_user", "Can delete user"),
            ("can_update_user", "Can update user"),
        )
