# from kino.serializers import ActorSerializer, MovieSerializer
# from unittest import TestCase
# from kino.models import Actor, Movie
#
# class TestActorSerializer(TestCase):
#     def setUp(self) -> None:
#         self.actor = Actor.objects.create(name="Amir Khan", gender="Male", birth_date="1975-06-15")
#     def test_data(self):
#         data = ActorSerializer(self.actor).data
#         assert data["id"] is not None
#         self.assertIsNotNone(data["id"])
#         self.assertEqual(data["name"], "Amir Khan")
#         assert data["name"] == "Amir Khan"
#         assert data["gender"] == "Male"
#
# class TestMovieSerializer(TestCase):
#     def setUp(self) -> None:
#         self.actor = Actor.objects.create(name="Amir Khan", gender="Male", birth_date="1975-06-15")
#
#         self.movie = Movie.objects.create(title="Nothing", genre="horror", date="1999-11-16")
#         self.movie.actors.add(self.actor)
#     def test_data(self):
#         data = MovieSerializer(self.movie).data
#         assert data["id"] is not None
#         self.assertEqual(data["title"], "Nothing")
#         assert data["genre"] == "horror"