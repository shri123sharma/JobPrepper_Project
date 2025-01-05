from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class RegisterView(APIView):
    def post(self,request):
        user_data=request.data
        serializer=RegisterSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class LoginView(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({
                'message': 'Login successful',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    
class LogoutView(APIView):
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Logout successful'}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleListCreateApiView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,*args,**kwargs):
        try:
            article_data=Article.objects.all()
            serializer=ArticleSerializer(article_data,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    def post(self,request,*args,**kwargs):
        try:
            article_data=request.data
            serializer=ArticleSerializer(data=article_data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Article objects sucessfully added","data":serializer.data},status=status.HTTP_201_CREATED) 
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        except:
            pass

class ArticleRetriveUpdateDeleteApiView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,pk,*args,**kwargs):
        try:
            article_obj=Article.objects.get(id=pk)
            serializer=ArticleSerializer(article_obj)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,pk,*args,**kwargs):
        try:
            article_obj=Article.objects.get(id=pk)
            serializer=ArticleSerializer(article_obj,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Update data is sucessfully","data":serializer.data},status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk,*args,**kwargs):
        try:
            article_obj=Article.objects.get(id=pk)
            article_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class LikeAPIView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request,article_id,*args,**kwargs):
        try:
            article_obj=Article.objects.get(id=article_id)
            like,created=Like.objects.get_or_create(user=request.user,article=article_obj)
            if not created:
                like.delete()
                return Response({"message": "Like removed"}, status=status.HTTP_200_OK)
            return Response({"message": "Article liked"}, status=status.HTTP_201_CREATED)
        except Article.DoesNotExist:
            return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)
        
class CommentAPIView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request,article_id,*args,**kwargs):
        try:
            article_obj=Article.objects.get(id=article_id)
            serializer=CommentSerilaizer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        except Article.DoesNotExist:
             return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)