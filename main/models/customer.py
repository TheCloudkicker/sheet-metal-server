from django.db import models
from .common import BaseModel


class Customer(BaseModel):
    name = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return f"Customer({self.id}) {self.name}"
