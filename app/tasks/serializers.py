from rest_framework import serializers
from app.tasks.models import Task
from app.tiles.models import Tile


class TaskTileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tile
        fields = ['id', 'launch_date', 'status']


class TaskSerializer(serializers.ModelSerializer):
    tile = TaskTileSerializer(
        required=False
    )

    class Meta:
        model = Task
        fields = ['id', 'title', 'order', 'type', 'description', 'created', 'updated', 'tile']
