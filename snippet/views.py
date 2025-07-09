from snippet.models import Snippet
from snippet.serializers import SnippetSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    lookup_field = 'pk'
    
@api_view(["POST"])
def login(request):
    return Response({})

@api_view(["POST"])
def signup(request):
    return Response({})

@api_view(["POST"])
def test_token(request):
    return Response({})