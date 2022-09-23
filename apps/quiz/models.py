import random
from django.db import models
from django.conf import settings
from shared.django.model import BaseModel



class Quiz(BaseModel):
    """ Quiz Table to store the quiz data """
    QUIZ_TYPE_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
    )
    host_id = models.PositiveBigIntegerField(default=random.randint(1111111134, 9999999999), unique=True)
    title = models.CharField(max_length=200)
    meta_title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    summary = models.TextField("The summary to mention the key highlights", max_length=200, blank=True)
    quiz_type = models.PositiveSmallIntegerField(default=1)
    score = models.PositiveSmallIntegerField(default=0)
    published = models.BooleanField(default=True)
    published_at = models.DateTimeField("need set when quiz published=True after need set date and time automatically for this model field ", auto_now_add=True)
    starts_at = models.DateTimeField("when starts a quiz", auto_now_add=True)
    ends_at = models.DateTimeField("when starts a quiz", auto_now_add=True)
    content = models.CharField(max_length=200)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Quizzes"
        verbose_name_plural = "Quiz"

class QuizMeta(models.Model):
    """ store additional information of tests or quiz including the quiz banner URL """
    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=300)

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = "Quiz Metas"
        verbose_name_plural = "Quiz Meta"

class Question(BaseModel):
    """ Store the questions related to tests and quizzes"""
    SINGLE_CHOICE = "single"
    MULTIPLE_CHOICE = 'multiple'
    SELECT_CHOICE = 'select'
    FILLING_CHOICE = "filling"
    QUESTION_CHOICES = (
        (SINGLE_CHOICE, 'single'),
        (MULTIPLE_CHOICE, 'multiple'),
        (SELECT_CHOICE, 'select'),
        (FILLING_CHOICE, 'filling'),
    )
    EASY_LEVEL = "easy"
    MEDIUM_LEVEL = "medium"
    HARD_LEVEL = "hard"
    EXPERT_LEVEL = "expert"
    LEVEL_CHOICES = (
        (EASY_LEVEL, 'easy'),
        (MEDIUM_LEVEL, 'medium'),
        (HARD_LEVEL, 'hard'),
        (EXPERT_LEVEL, 'expert'),

    )

    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL, null=True)
    question_type = models.CharField(max_length=50, choices=QUESTION_CHOICES, default=SINGLE_CHOICE)
    active = models.BooleanField(default=False)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES, default=EASY_LEVEL)
    score = models.IntegerField("only selective questions are active at a time and the total score of the active questions is equal to the quiz score before publishing the quiz", default=0)
    content = models.TextField(max_length=300)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Questions"
        verbose_name_plural = "Question"


class Answer(BaseModel):
    """ Store the answers of single-choice, multiple-choice and select type questions"""
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, related_name='answer_quiz')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, related_name='answer_questions')
    active = models.BooleanField(default=False)
    correct = models.BooleanField(default=False)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Answers"
        verbose_name_plural = "Answer"

class QuizTake(BaseModel):
    """ Track the enrollment and timing of user attempts to the quizzes"""

    ENROLLED = "enrolled"
    STARTED = "started"
    PAUSED = "paused"
    FINISHED = "finished"
    DECLARED = "declared"
    STATUS_CHOICES = (
        (ENROLLED, 'enrolled'),
        (STARTED, 'started'),
        (PAUSED, 'paused'),
        (FINISHED, 'finished'),
        (DECLARED, 'declared'),

    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='quiz_take')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="quiz_take")
    status = models.CharField(max_length=200, choices=STATUS_CHOICES)
    score = models.IntegerField("Total score obtained by the user", default=0)
    starts_at = models.DateTimeField("when starts a quiz", auto_now_add=True)
    finished_at = models.DateTimeField("when starts a quiz", auto_now_add=True)
    content = models.CharField("The column used to store the take remarks", max_length=200)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "QuizTakes"
        verbose_name_plural = "QuizTake"

class TakeAnswer(BaseModel):
    """Take Answer Table can be used to store the answers selected by the user while taking the quiz"""
    quiz_take = models.ForeignKey(QuizTake, on_delete=models.PROTECT, related_name="take_answer")
    answer = models.ForeignKey(Answer, on_delete=models.PROTECT, related_name="take_answer")
    active = models.BooleanField(default=False)
    content = models.CharField("The column used to store the answer in case of input or textarea type of questions", max_length=200)

    def __str__(self):
        return self.content
        
    class Meta:
        verbose_name = "TakeAnswers"
        verbose_name_plural = "TakeAnswer"
