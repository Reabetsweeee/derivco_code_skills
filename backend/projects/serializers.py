from rest_framework import serializers
from .models import Project 

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = ['id', 'owner', 'title', 'description', 'status', 'tech_stack', 'github_url', 'created_at', 'updated_at']