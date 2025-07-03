from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)  # To handle the user reference

    class Meta:
        model = Todo
        fields = ['id', 'text', 'date_created', 'completed', 'created_by']

    def create(self, validated_data):
        # Automatically set the created_by field to the current user
        user = self.context['request'].user  # Get the user from the request
        validated_data['created_by'] = user  # Assign the current user to created_by field
        return super().create(validated_data)
