from django.shortcuts import render
from rest_framework import viewsets
from .models import Article
from .permissions import IsAuthorOrReadOnly
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Create your views here.
