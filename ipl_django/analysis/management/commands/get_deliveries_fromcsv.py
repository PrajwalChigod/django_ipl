from django.core.management.base import BaseCommand, CommandError
from analysis.models import Matches, Deliveries
import csv

class Command(BaseCommand):
    help = 'Gets data from csv to the sqlite3 database'

    def handle(self, *args, **options):
        deliveries_file = 'deliveries.csv'

        with open(deliveries_file) as deliveires_csv:
            deliveries_reader = csv.DictReader(deliveires_csv)
            delivery_object_list = []
            for deliveries in deliveries_reader:
                print("d = ",deliveries)
                match_id = Matches.objects.get(id=deliveries['match_id'])
                delivery_object = Deliveries(
                        match_id = match_id,
                        inning = deliveries['inning'],
                        batting_team = deliveries['batting_team'],
                        bowling_team = deliveries['bowling_team'],
                        over = deliveries['over'],
                        ball = deliveries['ball'],
                        batsman = deliveries['batsman'],
                        non_striker = deliveries['non_striker'],
                        bowler = deliveries['bowler'],
                        is_super_over = deliveries['is_super_over'],
                        wide_runs = deliveries['wide_runs'],
                        bye_runs = deliveries['bye_runs'],
                        legbye_runs = deliveries['legbye_runs'],
                        noball_runs = deliveries['noball_runs'],
                        penalty_runs = deliveries['penalty_runs'],
                        batsman_runs = deliveries['batsman_runs'],
                        extra_runs = deliveries['extra_runs'],
                        total_runs = deliveries['total_runs'],
                        player_dismissed = deliveries['player_dismissed'],
                        dismissal_kind = deliveries['dismissal_kind'],
                        fielder = deliveries['fielder']
                )
                delivery_object_list.append(delivery_object)
            Deliveries.objects.bulk_create(delivery_object_list)