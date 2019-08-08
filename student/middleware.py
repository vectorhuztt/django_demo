#  @Author : Vector
#  @Email  : vectorztt@163.com
#  @Time   : 2019/8/8 15:42
# -----------------------------------------
import time

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class TimeItMiddleware(MiddlewareMixin):

    def process_request(self, request):
        self.start_time = time.time()
        return

    def process_view(self, request, func, *args, **kwargs):
        if request.path != reverse('index'):
            return None
        start = time.time()
        response = func(request)
        costed = time.time() - start
        print('process view %.2f s' % costed)
        return response

    def process_exception(self, request, exception):
        pass

    def process_template_response(self, request, response):
        return response

    def process_response(self, request, response):
        costed = time.time() - self.start_time
        print('process response %.2f s' % costed)
        return response


