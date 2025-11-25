from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel.name),
            User.objects.create(email='captainamerica@marvel.com', name='Captain America', team=marvel.name),
            User.objects.create(email='batman@dc.com', name='Batman', team=dc.name),
            User.objects.create(email='superman@dc.com', name='Superman', team=dc.name),
        ]

        # Activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date='2025-11-25')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2025-11-24')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date='2025-11-23')
        Activity.objects.create(user=users[3], type='Yoga', duration=50, date='2025-11-22')

        # Workouts
        Workout.objects.create(name='Full Body Blast', description='A full body workout', difficulty='Medium')
        Workout.objects.create(name='Cardio Burn', description='High intensity cardio', difficulty='Hard')

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
