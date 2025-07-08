from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippet.models import Snippet
from snippet.serializers import SnippetSerializer


@api_view(['GET', 'POST'])
def snippet_list(request):
    '''
    List all code snippets, or create a new snippet
    '''

    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        data = request.data
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_details(request, pk, format=None):
    '''
    View, update or delete for a particular data
    '''
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # VIEW
    if request.method == "GET":
        serializer = SnippetSerializer(snippet, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # UPDATE
    if request.method == "PUT":
        data = request.data
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    if request.method == "DELETE":
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)