from django.urls import path
from .views import index
from .api import GetFilePath

app_name = "blog"

urlpatterns = [
    path("", index)
]

urlpatterns += [path("api/", GetFilePath.as_view()),
                ]
