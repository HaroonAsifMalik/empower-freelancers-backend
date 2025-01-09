from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id', 
            'user', 
            'title', 
            'description', 
            'start_date', 
            'end_date', 
            'created_at', 
            'status', 
            'link', 
            'languages', 
            'frameworks'
        ]
        read_only_fields = ['id', 'created_at', 'user']
