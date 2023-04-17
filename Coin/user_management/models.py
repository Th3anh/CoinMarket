from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, web3_address):
        if web3_address is None:
            raise TypeError('Users must have an web3_address.')
        user = self.model(web3_address=web3_address)
        user.save()
        return user

    def create_superuser(self, web3_address):
        user = self.create_user(web3_address)
        user.is_superuser = True
        user.save()
        return user

        
class Web3User(AbstractBaseUser):
    web3_address = models.CharField(max_length=100,unique=True)
    is_superuser = models.BooleanField(default=False)
    is_broker = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    password = None
    objects = UserManager()

    USERNAME_FIELD = 'web3_address'
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser


class BNB(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField(max_length=1000)
    seller = models.ForeignKey(Web3User, on_delete = models.SET_NULL, null = True)

    RANK_CHOICES = [
    ('PACKAGE 1', 'GOLD'),
    ('PACKAGE 2', 'RUBY'),
    ('PACKAGE 3', 'PLATINUM'),
    ('PACKAGE 4', 'SAPPHIRE'),
    ('PACKAGE 5', 'DIAMOND'),
    ('PACKAGE 6', 'DOUBLE DIAMOND'),

    ]

    rank = models.CharField(choices=RANK_CHOICES, max_length=100)
    click_link = models.ManyToManyField(Web3User, related_name='user_click')

