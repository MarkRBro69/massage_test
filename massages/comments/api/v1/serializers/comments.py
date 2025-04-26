from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from comments.models import Comment


class CommentSerializer(ModelSerializer):
    child_comments = serializers.SerializerMethodField()
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

    def get_child_comments(self, obj):
        child_comments = Comment.objects.filter(parent_comment=obj)
        return CommentSerializer(child_comments, many=True).data
