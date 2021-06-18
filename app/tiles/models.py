from django.db import models


class Tile(models.Model):
    STATUS = [
        ('LIVE', 'LIVE'),
        ('PENDING', 'PENDING'),
        ('ARCHIVED', 'ARCHIVED')
    ]

    launch_date = models.DateField()

    status = models.CharField(
        max_length=8,
        choices=STATUS
    )

    def __str__(self):
        return f'Tile #{self.id}'
