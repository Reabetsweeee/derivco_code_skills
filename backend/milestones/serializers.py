from rest_framework import serializers
from .models import Milestone


class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = ['id', 'title', 'description', 'is_completed', 'completed_at', 'created_at']