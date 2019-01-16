from django.core.management.base import BaseCommand, CommandError
from analysis.models import Matches
import csv

class Command(BaseCommand):
    help = 'Gets data from csv to the sqlite3 database'

    def handle(self, *args, **options):
        matches_file = 'matches.csv'

        with open(matches_file) as matches_csv:
            matches_reader = csv.DictReader(matches_csv)
            for match in matches_reader:
                # print(match)
                match_created = Matches.objects.get_or_create(
                    id = match['id'],
                    season = match['season'],
                    city = match['city'],
                    date = match['date'],
                    team1 = match['team1'],
                    team2 = match['team2'],
                    toss_winner = match['toss_winner'],
                    result = match['result'],
                    dl_applied = match['dl_applied'],
                    winner = match['winner'],
                    win_by_runs = match['win_by_runs'],
                    win_by_wickets = match['win_by_wickets'],
                    player_of_match = match['player_of_match'],
                    venue = match['venue'],
                    umpire1 = match['umpire1'],
                    umpire2 = match['umpire2'],
                    umpire3 = match['umpire3']
                )
