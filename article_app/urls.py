from . import views
from django.urls import path
from .views import *

urlpatterns=[
    path('register/',views.RegisterView.as_view(),name="register"),
    path('login/',views.LoginView.as_view(),name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('article/',views.ArticleListCreateApiView.as_view(),name="article"),
    path('article/<int:pk>/',views.ArticleRetriveUpdateDeleteApiView.as_view(),name="article"),
    path('article/<int:article_id>/like/', LikeAPIView.as_view(), name='like-toggle'),
    path('article/<int:article_id>/comment/', CommentAPIView.as_view(), name='comment-create'),

]