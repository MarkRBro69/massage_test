from captcha.fields import CaptchaField
from captcha.serializers import CaptchaModelSerializer
from rest_framework import serializers

from comments.models import Comment


class CommentSerializer(CaptchaModelSerializer):
    child_comments = serializers.SerializerMethodField()
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_child_comments(self, obj):
        child_comments = Comment.objects.filter(parent_comment=obj)
        return CommentSerializer(child_comments, many=True).data

    def create(self, validated_data):
        validated_data.pop('captcha_code', None)
        validated_data.pop('captcha_hashkey', None)

        return Comment.objects.create(**validated_data)
