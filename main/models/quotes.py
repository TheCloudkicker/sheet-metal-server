from django.db import models
from .common import BaseModel


class Quote(BaseModel):
    name = models.CharField(max_length=256, null=False, blank=False)
    jobs = models.ManyToManyField("main.Job")

    def __str__(self):
        return f"Quote({self.id}) {self.name}"
