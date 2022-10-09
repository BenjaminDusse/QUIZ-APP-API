from email.policy import default
from django.db import models
from django.core.validators import RegexValidator
from core import settings
from django.templatetags.static import static
from shared.django.model import BaseModel

phone_regex = RegexValidator(
    regex=r"^998[0-9]{9}$",
    message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed.",
)


class ProfileManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user__is_active=True)


class Profile(BaseModel):
    MALE = "male"
    FEMALE = "female"

    GENDER_CHOICES = (
        (MALE, "male"),
        (FEMALE, "female"),
    )
    FREE_MEMBERSHIP_LEVEL = "Ad Supported - Free"
    PREMIUM_MEMBERSHIP_LEVEL = "Ad Supported - Free"
    MEMBERSHIP_LEVEL_CHOICES = (
        (FREE_MEMBERSHIP_LEVEL, "free"),
        (PREMIUM_MEMBERSHIP_LEVEL, "premium"),
    )

    phone = models.CharField(
        max_length=12, validators=[phone_regex], null=True, blank=True
    )

    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=MALE)
    photo = models.ImageField(
        upload_to="profile/",
        null=True,
        blank=True,
        default="profile/default.png",
    )
    level = models.IntegerField(default=1, blank=True, null=True)
    host = models.BooleanField(
        help_text="The flag to identify whether the user can host a quiz.",
        default=False,
    )

    objects = ProfileManager()
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="contacts",
        null=True,
        blank=True,
    )
    default_pic_mapping = {"male": "male_img.jpg", "female": "female_img.jpg"}
    dob = models.DateTimeField() # for test 

    @property
    def full_name(self):
        fullname = ""
        if self.first_name:
            fullname += f" {self.first_name}"
        if self.last_name:
            fullname += self.last_name
        return fullname

    # def save(self, *args, **kwargs): # here need write for dynamic default profile img
    #     if not self.photo:
    #         self.photo = 'images/{}'.format(self.photo[self.gender])
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ("-id",)
