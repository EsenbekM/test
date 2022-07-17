from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'title',
            'description',
            'cinema',
            'genres',
            ]
        

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProductDatailSerializer(serializers.ModelSerializer):
    film = FilmSerializer()

class MovieCreateValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=200)
    description = serializers.CharField()
    cinema = serializers.IntegerField()
    genres = serializers.ListField()

    def validate_cinema(self, cinema):
        try:
            Movie.objects.get(id=cinema)
        except Movie.DoesNotExist:
            raise ValidationError("This cinema doesn't exist!")

    def validate_title(self, title):
        if Movie.objects.filter(title=title):
            raise ValidationError("This movie already exist!")