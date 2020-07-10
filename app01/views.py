
from django.shortcuts import render,HttpResponse
import random
from utils.tencent.sms import send_sms_single
from django.conf import settings
# Create your views here.
def send_sms(request):
    """发送短信
        ?tpl=login
        ?tpl=register
    """
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

# 创建Modeform
from django import forms
from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class RegisterModeForm(forms.ModelForm):

    """重写或增加models中的文件"""
    # 重写电话号码，使用正则匹配使其格式为电话号码的格式
    mobile_phone = forms.CharField(label="手机",validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$','手机格式错误'),])
    # 重写密码格式
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    # 重写重复密码(如果没有就自动生成一个)
    confirm_password = forms.CharField(label='重复密码',widget=forms.PasswordInput())
    # 重写验证码:没有加widget会默认生成普通的input
    code = forms.CharField(label='验证码',widget=forms.TextInput())
    class Meta:
        model = models.UserInfo
        fields = "__all__"

    # 重写init方法，美化ModelForm格式
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items(): # name表示password，code等值，field表示其右边的函数
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入%s' % (field.label)

# 注册
def register(request):
    # 实例化ModelForm
    form = RegisterModeForm()
    return render(request, 'app01/register.html', {'form':form})