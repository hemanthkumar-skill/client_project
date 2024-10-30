# core/serializers.py

from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_by', 'created_at']
        extra_kwargs = {
            'created_by': {'read_only': True},
        }

class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']
        extra_kwargs = {
            'created_by': {'read_only': True},
        }
