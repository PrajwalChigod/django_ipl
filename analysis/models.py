from django.db import models

# Create your models here.

class Matches(models.Model):
    id = models.IntegerField(primary_key=True, max_length=250)
    season = models.IntegerField(max_length=100)
    city = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    toss_winner = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    dl_applied = models.IntegerField(max_length=100)
    winner = models.CharField(max_length=100)
    win_by_runs = models.IntegerField(max_length=100)
    win_by_wickets = models.IntegerField(max_length=100)
    player_of_match = models.CharField(max_length=100)
    venue = models.CharField(max_length=250)
    umpire1 = models.CharField(max_length=100)
    umpire2 = models.CharField(max_length=100)
    umpire3 = models.CharField(max_length=250)

    def __str__(self):
        return(f'{self.season}')


class Deliveries(models.Model):
    match_id = models.ForeignKey('Matches', on_delete=models.CASCADE)
    inning = models.IntegerField(max_length=100)
    batting_team = models.CharField(max_length=250)
    bowling_team = models.CharField(max_length=250)
    over = models.IntegerField(max_length=100)
    ball = models.IntegerField(max_length=100)
    batsman = models.CharField(max_length=100)
    non_striker = models.CharField(max_length=100)
    bowler = models.CharField(max_length=100)
    is_super_over = models.IntegerField(max_length=100)
    wide_runs = models.IntegerField(max_length=100)
    bye_runs = models.IntegerField(max_length=100)
    legbye_runs = models.IntegerField(max_length=100)
    noball_runs = models.IntegerField(max_length=100)
    penalty_runs = models.IntegerField(max_length=100)
    batsman_runs = models.IntegerField(max_length=100)
    extra_runs = models.IntegerField(max_length=100)
    total_runs = models.IntegerField(max_length=100)
    player_dismissed = models.CharField(max_length=100)
    dismissal_kind = models.CharField(max_length=100)
    fielder = models.CharField(max_length=100)

    def __str__(self):
        return(f'{self.match_id_id}')