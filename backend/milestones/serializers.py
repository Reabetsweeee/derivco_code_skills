from rest_framework import generics

from backend.users import serializers
from .models import Milestone

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = ['id', 'project', 'title', 'description', 'status', 'due_date', 'created_at', 'updated_at']    