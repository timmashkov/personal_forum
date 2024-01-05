from rest_framework import serializers
from . import models


class FileModelSerializer(serializers.ModelSerializer):
    file_path = serializers.SerializerMethodField()

    class Meta:
        model = models.PostFile
        fields = ["title", "file"]

    @staticmethod
    def get_file_path(obj):
        return obj.file if obj.file else None
