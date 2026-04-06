from rest_framework import serializers
from .models import Comment, CollabRequest


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'body', 'created_at']


class CollabRequestSerializer(serializers.ModelSerializer):
    requester = serializers.ReadOnlyField(source='requester.username')

    class Meta:
        model = CollabRequest
        fields = ['id', 'requester', 'message', 'status', 'created_at']