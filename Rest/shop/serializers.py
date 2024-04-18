# convert object to json
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers 

from django.contrib.auth import get_user_model
User = get_user_model()
class UserSerializer(ModelSerializer):
    class Meta:
        
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'is_active', 'is_superuser' ]
class ProductSerializer(ModelSerializer):
    user =  UserSerializer()

    class Meta:
        model = Product
        exclude = ['id']

class UploadProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ['id']

class SearchSerializer(serializers.Serializer):
    text = serializers.CharField()


class ReplyCommentSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%Y/%m/%d - %H:%i', read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    reply_count = serializers.SerializerMethodField()

    def get_reply_count(self, obj):
        return obj.replies.all().count()

    # def to_representation(self, instance):
    #     s = self.parent.parent.__class__(instance, context=self.context)
    #     return s.data

    class Meta:
        model = Comment
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%Y/%m/%d - %H:%i', read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    replies = ReplyCommentSerializer(many=True)
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ['parent']



