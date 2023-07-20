from django.urls import path

from todo.views import TodoListView, TodoCreateView, TodoView, LabelListView

urlpatterns = [
    path('todo-list/' , TodoListView.as_view()),
    path('create-todo/' , TodoCreateView.as_view()),
    path('todo/<pk>/' , TodoView.as_view()),
    path('label-list/' , LabelListView.as_view()),
]