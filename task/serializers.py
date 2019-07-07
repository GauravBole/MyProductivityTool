from rest_framework import serializers
from .models import Task, Comment


class TaskSerializer(serializers.ModelSerializer):
    task_comment = serializers.SerializerMethodField('comment')

    # Get task related all comments
    def comment(self, obj):
        return obj.comment_set.all().values()

    class Meta:
        model = Task
        fields = "__all__"
    

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"