from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    project_task = serializers.SerializerMethodField('task')

    # get projects related all tasks
    def task(self, obj):
        return obj.task_set.all().values()

    class Meta:
        model = Project
        fields = "__all__"

    def create(self, validated_data):
        validated_data.update({"user":self.context['request'].user}) # update validated data for logged user
        return Project.objects.create(**validated_data)





