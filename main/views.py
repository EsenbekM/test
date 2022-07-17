from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import FilmSerializer, MovieCreateValidateSerializer
from main.models import Movie


class CinemaListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination

class CinemaDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = FilmSerializer
    lookup_field = 'id'

# @api_view(['GET', 'POST'])  
# def cinema_list_view(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = FilmSerializer(movies, many=True)
#         return Response(data=serializer.data)
#     elif request.method == 'POST':
#         serializer = MovieCreateValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={'message': 'error', 'errors': serializer.errors})
#         title = request.data['title']
#         description = request.data['description']
#         cinema = request.data['cinema']
#         genres = request.data['genres']
#         movie = Movie.objects.create(
#             title=title, description=description, cinema_id=cinema,
#         )
#         movie.save()
#         movie.genres.set(genres)    
#         movie.save()
#         return Response("Movie succesfully added!")

# @api_view(['GET', 'PUT', 'DELETE'])
# def cinema_detail_view(request, id):
#     try:
#         movie = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={'eror':'Movie not found'})
#     if request.method == 'GET':
#         serializer = FilmSerializer(movie, many=False)
#         return Response(data=serializer.data)
#     elif request.method == 'PUT':
#         serializer = MovieCreateValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={'message': 'error', 'errors': serializer.errors})
#         movie.title == request.data['title']
#         movie.description == request.data['description']
#         movie.cinema == request.data['cinema']
#         movie.genres.set(request.data['genres'])
#         movie.save()
#         return Response(data={'massage': 'Movie updated!'})
#     else:
#         movie.delete()
        # return Response()
