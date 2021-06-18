from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('app.tasks.urls')),
    path('tiles/', include('app.tiles.urls'))
]
