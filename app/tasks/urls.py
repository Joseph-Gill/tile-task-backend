from django.urls import path
from app.tasks.views import ListAllTasks, ListAllTasksOrCreateTaskForSpecifiedTile, RetrieveUpdateDestroySpecifiedTask


urlpatterns = [
    path('all/', ListAllTasks.as_view(), name='list-all-tasks'),
    path('tile/<int:tile_id>/', ListAllTasksOrCreateTaskForSpecifiedTile.as_view(), name='list--create-task-specific-tile'),
    path('task/<int:task_id>/', RetrieveUpdateDestroySpecifiedTask.as_view(), name='retrieve-update-destroy-task')
]
