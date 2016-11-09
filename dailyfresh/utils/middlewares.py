from django.http.response import HttpResponse
import json
from .exceptions import EcomException


class UtilMiddleWare(object):

    def process_exception(self, request, exception):
        if isinstance(exception, EcomException):
            res = {'code': exception.code,
                   'message': exception.message}
        else:
            res = {'code': 500, 'message': '服务器内部错误!'}
        return HttpResponse(json.dumps(res), content_type='application/json')

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = 'http://localhost:8888'
        response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT'
        response['Access-Control-Allow-Credentials'] = 'true'
        response['Access-Control-Allow-HEADERS'] = 'X-Requested-With'
        if r'image/get' not in request.path:
            content = json.loads(str(response.content, encoding='utf-8'))
            content.update(is_login=request.user.is_authenticated())
            response.content = json.dumps(content)
        return response
