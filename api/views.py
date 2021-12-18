from rest_framework import serializers
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsAuthenticatetReadOnly
from django.contrib.auth import get_user_model
from articles.models import Articles
from .serializers import ArticlesSerializers, UserSerializers


class ListViewPage(ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializers

class UpdateViewPage(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatetReadOnly,)
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializers

class UserViewPage(ListCreateAPIView):
    permission_classes = (IsAuthenticatetReadOnly,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers

class UserDetailViewPage(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers