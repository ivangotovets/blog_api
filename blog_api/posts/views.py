from rest_framework import generics, permissions

from .models import Post
from .permissions import IsAuthorOrReadonly
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadonly,)
