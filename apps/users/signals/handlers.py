from django.dispatch import receiver
from accounts.signals import profile_created


@receiver(profile_created)
def on_profile_created(sender, **kwargs):
    print(kwargs)
    print(kwargs["profile"])
    print("Profile created successfully")