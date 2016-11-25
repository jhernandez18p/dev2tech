import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Account(models.Model):

    name =  models.CharField(max_length=50)
    duration = models.CharField(max_length=10, default='%Y%b%d')

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = ('Account type')
        verbose_name_plural = ('Account type')
        permissions = (
            ("can_create_account", "Can create account"),
            ("can_delete_account", "Can delete account"),
            ("can_update_account", "Can update account"),
        )



class User(models.Model):

    GENRE_CHOICE = (
        (1,('Hombre')),
        (2,('Mujer')),
    )

    intra_user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=200, blank=True)
    genre = models.IntegerField(choices=GENRE_CHOICE,default=1)
    account = models.ForeignKey(Account,on_delete=models.CASCADE,)
    avatar = models.ImageField(upload_to="user_account_avatar",blank=True)

    def __str__(self):

        return self.user_name()

    def user_name(self):
        return '%s %s' % (self.first_name,self.last_name)

    class Meta:

        verbose_name = ('User')
        verbose_name_plural = ('Users')
        permissions = (
            ("can_create_user", "Can create user"),
            ("can_delete_user", "Can delete user"),
            ("can_update_user", "Can update user"),
        )
