from django.contrib.auth import get_user_model

from rest_framework import viewsets

from .models import Post
from .permissions import IsAuthorOrReadonly
from .serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadonly,)


class UserViewSet(viewsets.ModelViewSet):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
