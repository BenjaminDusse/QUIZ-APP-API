import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from quiz.models import Question, Quiz
from users.models import User


class Command(BaseCommand):

    help = "This command creates questions"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many questions you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        questions = Question.objects.all()
        seeder.add_entity(
            Question,
            number,
            {
                "quiz": Quiz.objects.get(id=1),
                "question_type": lambda x: random.randint(1, 5),
                "active": True,
                "level": lambda x: random.randint(1, 5),
                "score": lambda x: random.randrange(40, 100, 10),
                "content": lambda x: seeder.faker.paragraph(),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} questions created!"))
