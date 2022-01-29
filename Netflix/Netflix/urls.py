
from django.contrib import admin
from django.urls import path, include
from kino.views import MovieRetrieveAPIView,MovieCreateAPIView, MovieDestroyAPIView, MovieUpdateAPIView, ActorListAPIView, ActorRetrieveAPIView, ActorCreateAPIView,ActorDestroyAPIView, ActorUpdateAPIView, MovieListAPIView
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Netflix API",
      default_version='v1',
      description="Netflix",
      contact=openapi.Contact(email="abdunabiabduvahobov86@gmail.com", ),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

ro = DefaultRouter()
# ro.register('actors', ActorAPIViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(ro.urls)),
    path('actor/', ActorListAPIView.as_view(), name='actor-list'),
    path('actorget/<int:pk>', ActorRetrieveAPIView.as_view(), name='actor-retrieve'),
    path('actor/add', ActorCreateAPIView.as_view(), name='actor-create'),
    path('actordel/<int:pk>', ActorDestroyAPIView.as_view(), name='actor-destroy'),
    path('actorput/<int:pk>', ActorUpdateAPIView.as_view(), name='actor-update'),
    path('movie/', MovieListAPIView.as_view(), name='movie-list'),
    path('movieget/<int:pk>', MovieRetrieveAPIView.as_view(), name='movie-retrieve'),
    path('movie/add', MovieCreateAPIView.as_view(), name='movie-create'),
    path('moviedel/<int:pk>', MovieDestroyAPIView.as_view(), name='movie-destroy'),
    path('movieput/<int:pk>', MovieUpdateAPIView.as_view(), name='movie-update'),
    #open API Documentation
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]
