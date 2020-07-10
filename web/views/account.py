"""
用户账户相关功能：注册、短信、登录、注销
"""
from django.shortcuts import render
from web.forms.account import RegisterModeForm
def register(request):
    # 实例化modelform
    form = RegisterModeForm()
    return render(request,'register.html',{'form':form})