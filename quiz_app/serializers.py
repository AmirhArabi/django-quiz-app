from rest_framework import serializers, filters
from .models import Question, UserResult, Category


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ('status',)
        read_only_fields = ('id',)


class CategorysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_name', 'id')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResult
        exclude = ('created_at', 'id')
