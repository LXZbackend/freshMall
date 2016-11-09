from django.http import JsonResponse, HttpResponse
import functools


def json_view(func):
    def wrapped(request, *args, **kwargs):
        data = func(request, *args, **kwargs)
        return JsonResponse(data)
    return wrapped


def string_view(func):
    def wrapped(request, *args, **kwargs):
        data = func(request, *args, **kwargs)
        return HttpResponse(data)
    return wrapped

