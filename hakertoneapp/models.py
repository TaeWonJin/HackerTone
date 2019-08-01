from django.db import models

class Team(models.Model):
    teamname = models.CharField(max_length = 20)
    howmany = models.IntegerField()
    howlong = models.IntegerField()

class TeamUser(models.Model):
    teamuser = models.CharField(max_length =20)
    userteam = models.CharField(max_length =20)