from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Book
from .serializers import *


class BookList(APIView):
    def get(self,request):
        book=Book.objects.all()
        book_serializer=BookSerializer(book,many=True)
        return Response(book_serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        data=request.data()
        book_serializer=BookSerializer(data=data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data,status=status.HTTP_201_CREATED)
        return Response(book_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class BookDetail(APIView):
    def get(self,request,pk):
        try:
            book=Book.object.get(pk=pk)
            book_serializer=BookSerializer(book)
            return Response(book_serializer.data,status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,pk):
        book=Book.objects.get(pk=pk)
        book_seralizer=BookSerializer(book,data=request.data)
        if book_seralizer.is_valid():
            book_seralizer.save()
            return Response(book_seralizer.data,status=status.HTTP_200_OK)
        return Response(book_seralizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# Create your views here.
