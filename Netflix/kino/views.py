from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from .models import *
from .serializers import *

class ActorListAPIView(ListAPIView):
    search_fields = ['name']
    ordering_fields = ['name', 'gender', 'birth_date']
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()
class ActorCreateAPIView(CreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
class ActorRetrieveAPIView(RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
class ActorDestroyAPIView(DestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
class ActorUpdateAPIView(UpdateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
# class MovieAPIViewSet(ModelViewSet):
#     serializer_class = MovieSerializer
#     queryset = Movie.objects.all()
#     search_fields = ['title']
#     ordering_fields = ['title', 'genre', 'date', 'actors']
#     filter_backends = (filters.SearchFilter, filters.OrderingFilter)
#     @action(methods=['GET'], detail=True, url_path='actors')
#     def get_actor(self, request, *args, **kwargs):
#         movie = self.get_object()
#         actors = Actor.objects.filter(movie = movie)
#         ser = ActorSerializer(actors, many=True)
#         return Response(ser.data)
#     @action(methods=['POST'], detail=True, url_path='actor')
#     def post_actor(self, request, *args, **kwargs):
#         movie = self.get_object()
#         actor = request.data
#         actor['movie'] = movie.id
#         ser = ActorSerializer(data=actor)
#         if ser.is_valid():
#             ser.save()
#         return Response(ser.data)
#
class MovieListAPIView(ListAPIView):
    queryset=Movie.objects.all()
    serializer_class = MovieSerializer
    search_fields = ['name']
    ordering_fields = ['name', 'gender', 'birth_date']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
class MovieCreateAPIView(CreateAPIView):
    queryset=Movie.objects.all()
    serializer_class = MovieSerializer
class MovieRetrieveAPIView(RetrieveAPIView):
    queryset=Movie.objects.all()
    serializer_class = MovieSerializer
class MovieDestroyAPIView(DestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class = MovieSerializer
class MovieUpdateAPIView(UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer