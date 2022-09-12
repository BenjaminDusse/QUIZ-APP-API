from django.db import models
from django.db.models import QuerySet


class BaseQuerySet(models.QuerySet):

    def delete(self):
        self.update(is_active=False)


class DeleteManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return BaseQuerySet(self.model).filter(is_active=True)


