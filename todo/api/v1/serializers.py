from rest_framework import serializers
from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = ("id", "title", "owner", "done", "created_date")

    def get_user(Self, obj):
        """
        Getting the user when creating and editing a post.
        """
        return {obj.owner.username}
