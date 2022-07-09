from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from datetime import timedelta


class UserManager(BaseUserManager):
    """Help Django works with our custom model"""

    def create_user(self, email, name, password):
        """create BLMS_API"""
        if not email:
            raise ValueError('Email address is compulsory for a BLMS_API')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """create superuser"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model of the application"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user_type = models.CharField(max_length=10)
    duration = models.DurationField(default=timedelta(0))
    login_count = models.IntegerField(default=0)
    online = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """function to get full name"""

        return self.name

    def get_short_name(self):
        """function to get short name"""
        return self.name

    def __str__(self):
        return "[email = " + self.email + ", name = " + self.name + ", is_active = " + str(self.is_active) + "]"


class Team(models.Model):
    """Teams Model"""

    name = models.CharField(max_length=255, unique=True)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)


class Match(models.Model):
    """Match Model"""

    name = models.CharField(max_length=255)
    winners = models.OneToOneField(Team, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField()


class MatchScore(models.Model):
    """Bridge table for Scores of the matches"""

    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)


class Player(models.Model):
    """Player Model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=2, decimal_places=2)
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    average_score = models.DecimalField(max_digits=5, decimal_places=3)
    games_count = models.IntegerField(default=0)


class Coach(models.Model):
    """Coach Model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.OneToOneField(Team, on_delete=models.CASCADE)


class MatchPlayers(models.Model):
    """Bridge table for players who played for matches"""

    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score = models.IntegerField()

