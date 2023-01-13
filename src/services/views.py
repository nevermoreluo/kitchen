from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request: WSGIRequest) -> HttpResponse:
    """
    index页面示例
    Args:
        request (WSGIRequest): http请求入参

    Returns:
        HttpResponse: http返回
    """
    return HttpResponse("Hello, world. You're at the polls index.")
