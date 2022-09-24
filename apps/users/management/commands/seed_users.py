import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users.models import User


class Command(BaseCommand):

    help = "This command creates users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many users you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(
            User,
            number,
            {
                "email": lambda x: seeder.faker.ascii_safe_email(),
                "username": lambda x: seeder.faker.first_name(),
                "password": lambda x: seeder.faker.ean(length=8),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))
