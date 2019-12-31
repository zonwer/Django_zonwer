from django.shortcuts import render,redirect
from django.views import View
from django import http
import  re
from .models import User
from django.contrib.auth.models import User
from django.contrib.auth import login
from meiduo_mall.utils.response_code import RETCODE

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
        # return render(request, 'register_vue.html')
    def post(self,request):
        # 接收
        username= request.POST.get('user_name')
        password = request.POST.get('pwd')
        password2 = request.POST.get('cpwd')
        mobile = request.POST.get('msg_code')
        sms_code = request.POST.get('allow')
        allow = request.POST.get()
        # 验证
        # 1.判断数据非空:all 方法,内部遍历是否为空,只要有一个为(None,空值,0),则返回为false,加not表示有空值
        if not all([username,password,password2,mobile,sms_code, allow]):
            return http.HttpResponseForbidden("填写数据不完整")
        # 2.用户名
        if not re.match('^[a-zA-Z0-9_-]{5,20}$',username):
            return http.HttpResponseForbidden("用户名格式错误")
        if User.objects.filter(username=username).count()>0:
            return http.HttpResponseForbidden("用户名已经存在")
        # 3.密码
        if not re.match("^[0-9A-Za-z]{8,20}$",password):
            return http.HttpResponseForbidden('密码格式不对')
        # 4.确认密码认证
        if password !=password2:
            return http.HttpResponseForbidden("两个密码不一致")
        # 5 手机号的认证
        if not re.match('^1[3456789]\d{9}$',mobile):
            return http.HttpResponseForbidden('手机号码不正确')
        if User.objects.filter(mobile=mobile).count()>0:
            return http.HttpResponseForbidden("手机号码已经存在")
        # 图形验证码

        # 处理
        # 1.创建用户对象,creat_user相比crate(username=username,password=password的优势,是会对密码进行加密处理,防止信息泄露
        user = User.objects.create_user(
            username=username,
            password=password,
            mobile=mobile
        )
        # 2.状态保持
        login(request,user)


        # 响应
        return redirect("/")


class UsernameCountView(View):
    def get(self,request,username):
        # 接受:通过理由在路径中提取
        # 验证:路由的正则表达式
        count = User.objects.filter(username=username).count()

        return http.JsonResponse({
            'count':count,
            'code':RETCODE.OK,
            'errmsg':'OK'
        })



class MobileCountView(View):
    def get(self,request,mobile):
        count =  User.objects.filter(mobile=mobile).count()
        return http.JsonResponse({
            'count': count,
            'code': RETCODE.OK,
            'errmsg': 'OK'
        })

