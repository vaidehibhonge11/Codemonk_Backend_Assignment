from rest_framework import serializers
from .models import CustomUser, Paragraph, WordIndex

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'email', 'dob', 'created_at', 'modified_at', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'text', 'created_at', 'modified_at']

    def create(self, validated_data):
        paragraph = Paragraph.objects.create(**validated_data)
        paragraph.tokenize_and_index_text()
        return paragraph
