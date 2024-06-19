from rest_framework import serializers

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class GenreRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name","last_name", "full_name"]


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]

class MovieRetrieveSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ["title", "description", "duration", "genres", "actors"]

class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
    )
    actors = (serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='__str__'
    ))

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieSessionSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title')
    cinema_hall_name = serializers.CharField(source='cinema_hall.name' )
    cinema_hall_capacity = serializers.IntegerField(source='cinema_hall.capacity')

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie_title", "cinema_hall_name", "cinema_hall_capacity"]

class MovieSessionRetrieveSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)
    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]
