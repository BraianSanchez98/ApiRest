from pyexpat import model
from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Project
        fields = ('id', 'title', 'description','technology', 'created_at')
        read_only_flelds = ('created_at',)