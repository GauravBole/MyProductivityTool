from django.urls import path

from .views import TaskApiView, TaskDetailApiView, CommentApiView
app_name = "task"
urlpatterns = [
    path('task/', TaskApiView.as_view(), name="task"),
    path('task/<int:pk>', TaskDetailApiView.as_view(), name="task"),
    path('comment/', CommentApiView.as_view(), name="comment"),
]