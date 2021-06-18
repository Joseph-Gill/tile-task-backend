from rest_framework import serializers
from app.tasks.serializers import TaskSerializer
from app.tiles.models import Tile


class TileSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(
        required=False,
        many=True
    )

    class Meta:
        model = Tile
        fields = ['id', 'launch_date', 'status', 'tasks']
