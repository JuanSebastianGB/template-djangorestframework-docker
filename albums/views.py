from django.shortcuts import render
from rest_framework import viewsets
from .models import Album, Track
from .serializer import AlbumSerializer, TrackSerializer


# Create your views here.
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
