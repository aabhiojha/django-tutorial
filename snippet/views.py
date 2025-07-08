from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from snippet.models import Snippet
from snippet.serializers import SnippetSerializer
from django.http import Http404

class SnippetList(APIView):
    '''
    List all snippets, or create a new snippet
    '''
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        data = request.data
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetails(APIView):
    '''
    View, update or delete for a particular data
    '''
    def get_object(self, pk):
        try:
            snippet = Snippet.objects.get(pk=pk)
            return snippet
        except:
            raise Http404

    # VIEW
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # UPDATE
    def put(self, request, pk, format=None):
        data = request.data
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)