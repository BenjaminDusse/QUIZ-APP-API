import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from quiz.models import Answer, Quiz, Question
from users.models import User


class Command(BaseCommand):

    help = "This command creates answers"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many answers you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        questions = Question.objects.all()
        seeder.add_entity(
            Answer,
            number,
            {
                "quiz": Quiz.objects.get(id=1),
                "question": lambda x: random.choice(questions),
                "active": True,
                "correct": lambda x: random.randrange(0, 2),
                "content": lambda x: seeder.faker.text(max_nb_chars=80),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} answers created!"))

