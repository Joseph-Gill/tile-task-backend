from django.db import models
from app.tiles.models import Tile


class Task(models.Model):
    TYPE = [
        ('SURVEY', 'SURVEY'),
        ('DISCUSSION', 'DISCUSSION'),
        ('DIARY', 'DIARY')
    ]

    title = models.TextField()

    order = models.TextField()

    description = models.TextField()

    type = models.CharField(
        max_length=10,
        choices=TYPE
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    tile = models.ForeignKey(
        to=Tile,
        on_delete=models.CASCADE,
        related_name='tasks',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Task #{self.id} for Tile #{self.tile.id}'
