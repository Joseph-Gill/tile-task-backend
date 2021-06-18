from django.urls import path
from app.tiles.views import ListAllTiles, CreateNewTile, RetrieveUpdateDestroySpecificTile


urlpatterns = [
    path('all/', ListAllTiles.as_view(), name='list-all-tiles'),
    path('tile/create/', CreateNewTile.as_view(), name='create-tile'),
    path('tile/<int:tile_id>/', RetrieveUpdateDestroySpecificTile.as_view(), name='retrieve-update-destroy-tile')
]
