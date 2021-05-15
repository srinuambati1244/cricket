from django.db import models


class Team(models.Model):
    team_id = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    logo_url = models.ImageField(upload_to='media/')
    club_state = models.CharField(max_length=250)


    def __str__(self):
        return self.name


class Player(models.Model):
    player_id = models.IntegerField()
    firstname = models.CharField(max_length=230)
    lastname = models.CharField(max_length=200)
    image_url = models.ImageField(upload_to='media/')
    jersey_id = models.IntegerField(default=0)
    country = models.CharField(max_length=100)
    matches = models.IntegerField()
    runs = models.IntegerField()
    highest_scores = models.IntegerField(default=0)
    fifties = models.IntegerField()
    hundreds = models.IntegerField(max_length=100)
    wickets = models.IntegerField(max_length=150)
    player_type = models.CharField(max_length=300)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


    def __str__(self):
        return self.jersey_id


class Matches_points(models.Model):
    team_matches = models.TextField(max_length=200)
    points = models.IntegerField()




