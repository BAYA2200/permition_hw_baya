from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .serializers import TweetSerializer, CommentSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .permissions import IsAuthorPermission
from .models import Tweet, Comment


class TweetViewSet(ModelViewSet):
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAuthorPermission, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAuthorPermission, ]

    def comment_create(self, serializers):
        serializers.save(user=self.request.user)