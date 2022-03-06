# <project>/<app>/management/commands/seed.py
from blog.models import Post, User, Profile
from django.core.management.base import BaseCommand
import random
import logging
from django.utils import timezone
from faker import Faker
fake = Faker()

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    logging.info("Delete Address instances")
    Post.objects.all().delete()
    User.objects.all().delete()
    Profile.objects.all().delete()


def create_address():
    """Creates an address object combining different elements from the list"""
    logging.info("Creating address")
    title = ["Bakers Street", "Rajori Gardens",
             "Park Street", "MG Road", "Indiranagar"]
    body = [
        "Just do it!", "Nice post", "Good job!", "What do you doing?", "Django id fun"
    ]
    author=User.objects.create(username=fake.user_name(), password=fake.password()),
    Profile.objects.create(user=author[0], images_url=fake.image_url(), website=fake.url())

    post = Post(
        author=author[0],
        title=' '.join(fake.words()),
        body=' '.join(fake.texts()),
        published_at=timezone.now()
    )
    post.save()
    logging.info("{} address created.".format(post))
    return post


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # Creating 15 posts
    for i in range(15):
        create_address()
