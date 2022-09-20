import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from accounts.models import Profile


class Command(BaseCommand):

    help = "This command creates profiles"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many profiles you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = User.objects.all()
        # created_user = User.objects.create(
        #     username=lambda x: seeder.faker.name(),
        #     password=lambda x: seeder.faker.ean(),
        # )

        profile = seeder.add_entity(
            Profile,
            number,
            {
                "first_name": lambda x: seeder.faker.name(),
                "last_name": lambda x: seeder.faker.name(),
                "gender": lambda x: random.choice(("male", "female")),
                "phone": lambda x: seeder.faker.msisdn(),
                "email": lambda x: seeder.faker.email(domain="com"),
                "user": random.choice(users),
            },
        )
        print(profile)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} profiles created!"))
