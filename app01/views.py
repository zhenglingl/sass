from django.shortcuts import render,HttpResponse
import random
from utils.tencent.sms import send_sms_single
from django.conf import settings
# Create your views here.
def send_sms(request):
    """发送短信"""
    tpl = request.GET.get('tpl')
    template_id = settings.TENCENT_SMS_TEMPLATE(tpl)
    if not template_id:
        return HttpResponse('不存在')

    code = random.randrange(1000,9999)
    res = send_sms_single('18800253559',template_id,[code,])
    if res['result'] == 0:
        return HttpResponse('ok')
    else:
        return HttpResponse(res['errmsg'])

