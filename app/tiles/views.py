from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from app.tiles.models import Tile
from app.tiles.serializers import TileSerializer


class ListAllTiles(ListAPIView):
    """
    List All Tiles
    """
    queryset = Tile.objects.all()
    serializer_class = TileSerializer
    permission_classes = []


class CreateNewTile(CreateAPIView):
    """
    Create a new Tile
    """
    serializer_class = TileSerializer
    permission_classes = []


class RetrieveUpdateDestroySpecificTile(RetrieveUpdateDestroyAPIView):
    """
    get:
    List a specified Tile

    update:
    Update a specified Tile

    delete:
    Delete a specified Tile
    """
    http_method_names = ['get', 'patch', 'delete']
    serializer_class = TileSerializer
    queryset = Tile.objects.all()
    lookup_url_kwarg = 'tile_id'
    permission_classes = []
