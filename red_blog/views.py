from django.shortcuts import render


def index(request):
    return render(request, "red_blog/base.html")
