from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Workout, Activity, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
        ]

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Pushup workout', difficulty='Easy')
        running = Workout.objects.create(name='Running', description='Running workout', difficulty='Medium')
        yoga = Workout.objects.create(name='Yoga', description='Yoga session', difficulty='Easy')

        # Create Activities
        Activity.objects.create(user=users[0], workout=pushups, date=timezone.now().date(), duration_minutes=30, score=100)
        Activity.objects.create(user=users[1], workout=running, date=timezone.now().date(), duration_minutes=45, score=150)
        Activity.objects.create(user=users[2], workout=yoga, date=timezone.now().date(), duration_minutes=60, score=120)
        Activity.objects.create(user=users[3], workout=pushups, date=timezone.now().date(), duration_minutes=20, score=80)

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], total_score=100, rank=2)
        Leaderboard.objects.create(user=users[1], total_score=150, rank=1)
        Leaderboard.objects.create(user=users[2], total_score=120, rank=3)
        Leaderboard.objects.create(user=users[3], total_score=80, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
