from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BolgsSerializer, Blogs

class BlogList(APIView):
    def get(self, request):
        articles = Blogs.objects.all()
        serialize = BolgsSerializer(articles, many=True)
        return Response(serialize.data)
