from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from todo.models import Todo, Label
from todo.serializers import TodoSerializer, TodoCreateSerializer, LabelSerializer


class TodoListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['deadline', 'completed']
    search_fields = ['title', ]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)


class TodoCreateView(CreateAPIView):
    serializer_class = TodoCreateSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Todo.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user, )


class LabelListView(ListAPIView):
    serializer_class = LabelSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        return Label.objects.filter(user=user)
