from django.core.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import *

class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
    def validate_name(self, value):
        if len(value) <= 2:
            raise ValidationError("Name should consist of more than 2 letters")
        return value

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
    def validate_title(self, value):
        if len(value) <= 3:
            raise ValidationError('The title of the movie must contain at least four letters')
        return value
