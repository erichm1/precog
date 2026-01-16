import uuid
from django.db import models

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    AGE_RANGES = [
        ('0-17', '0-17'),
        ('18-25', '18-25'),
        ('26-40', '26-40'),
        ('41-60', '41-60'),
        ('60+', '60+'),
    ]

    age_range = models.CharField(max_length=10, choices=AGE_RANGES)
    gender = models.CharField(max_length=20, blank=True, null=True)

    total_occurrences = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["age_range"]),
        ]