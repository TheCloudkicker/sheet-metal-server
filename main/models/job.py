from django.db import models
from .common import BaseModel


class Job(BaseModel):
    name = models.CharField(max_length=256, null=False, blank=False)
    customer = models.ForeignKey(
        "main.Customer", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return f"Customer({self.id}) {self.name}"
