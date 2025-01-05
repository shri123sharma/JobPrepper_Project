from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }
    
class Article(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    author=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,related_name="user_article")

    def __str__(self):
        return f"this is article {self.title}-{self.content}"
    
class Like(models.Model):
    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    article=models.ForeignKey(Article,null=True,blank=True,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} liked {self.article.title}"
    
class Comment(models.Model):
    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    article=models.ForeignKey(Article,null=True,blank=True,related_name="comments",on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} comment {self.article.title}" 

