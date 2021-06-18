from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from app.tasks.models import Task
from app.tasks.serializers import TaskSerializer
from app.tiles.models import Tile
from rest_framework.response import Response


class ListAllTasks(ListAPIView):
    """
    List all Tasks
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = []


class ListAllTasksOrCreateTaskForSpecifiedTile(ListCreateAPIView):
    """
    get:
    List all Tasks for a specified Tile

    post:
    Create a new Task for a specified Tile
    """
    queryset = Tile.objects.all()
    serializer_class = TaskSerializer
    permission_classes = []
    lookup_url_kwarg = 'tile_id'

    def list(self, request, *args, **kwargs):
        target_tile = self.get_object()

        page = self.paginate_queryset(target_tile.tasks.all())
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(target_tile.tasks.all(), many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        target_tile = self.get_object()
        new_task = Task(
            **serializer.validated_data
        )
        new_task.save()
        target_tile.tasks.add(new_task)


class RetrieveUpdateDestroySpecifiedTask(RetrieveUpdateDestroyAPIView):
    """
    get:
    List a specified Task

    update:
    Update a specified Task

    delete:
    Delete a specified Task
    """
    http_method_names = ['get', 'patch', 'delete']
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_url_kwarg = 'task_id'
    permission_classes = []
