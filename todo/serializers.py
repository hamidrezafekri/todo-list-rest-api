from rest_framework import serializers, filters

from todo.models import Todo, Label


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ['user']


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'deadline', 'label']


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['name']
