from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist

from red_blog import serializers
from red_blog.models import PostFile


class GetFilePath(APIView):
    @staticmethod
    def get(request):
        code = request.GET.get("code")
        try:
            file = PostFile.objects.get(code=code)
            file.increment_count()
            serialized_data = serializers.FileModelSerializer(file)
            return Response(serialized_data.data)
        except ObjectDoesNotExist:
            return Response(None, status=404)
