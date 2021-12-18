from rest_framework import fields, serializers
from django.contrib.auth import get_user_model
from articles.models import Articles

class ArticlesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articles 
        fields = ('id', 'title', 'summary', 'date', 'photo', 'author')



class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'is_staff')