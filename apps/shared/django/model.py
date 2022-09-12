from django.db import models

from shared.django.queryset import DeleteManager


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DeleteModel(models.Model):
    is_active = models.BooleanField(default=True)

    objects = DeleteManager()

    class Meta:
        abstract = True

    def delete(self, **kwargs):
        self.is_active = False
        self.save()

