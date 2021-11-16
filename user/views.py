from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import User
import hashlib


# Create your views here.

# ---------- 注册接口模块 -----------
def register(request):
    if request.method == "GET":
        return render(request, 'user/register.html')

    elif request.method == "POST":
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')

        # 判断用户名不为空
        if not username or not password_1:
            return HttpResponse('数据不能为空')

        # 用户名不能为汉字
        for name in username:
            if '\u4e00' <= name <= '\u9fff':
                return HttpResponse('用户名不允许出现汉字')

        # 密码不能小于6位数
        if len(password_1) < 6:
            return HttpResponse('密码不能小于6位数')

        # 重复验证密码
        if password_1 != password_2:
            return HttpResponse('输入的密码不一致')

        # 查重用户名
        old_user = User.objects.filter(username=username)
        if old_user:
            return HttpResponse('该用户名已被注册')

        # 密码加密MD5
        md5 = hashlib.md5()
        md5.update(password_1.encode())
        password_hash = md5.hexdigest()

        try:
            # 存储用户用户和密码到数据库
            User.objects.create(username=username, password=password_hash)

        except Exception as e:
            print(f'create error is {e.args}')

        return HttpResponse('注册成功')


# ---------- 登录接口模块 -----------
def login(request):
    if request.method == "GET":
        # 检查检查session判断是否登录过
        if 'username' in request.session and 'uid' in request.session:
            return HttpResponseRedirect('/note/add_note')

        username = request.COOKIES.get('username')
        uid = request.COOKIES.get('uid')
        # 检查cookies
        if username and uid:
            request.session['username'] = username
            request.session['uid'] = uid
            return HttpResponseRedirect('/note/add_note')

        return render(request, 'user/login.html')

    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            # 检查是否注册
            old_user = User.objects.get(username=username)
        except Exception as e:
            return HttpResponse('用户名或密码错误')

        # MD5生成
        md5 = hashlib.md5()
        md5.update(password.encode())
        password_hash = md5.hexdigest()

        # 校验密码
        if password_hash != old_user.password:
            return HttpResponse('用户名或密码错误')

        resp = HttpResponseRedirect('/note/add_note')

        # 在session保存登录状态
        request.session['uid'] = old_user.id
        request.session['username'] = old_user.username

        try:
            # 根据用户的选择在cookie中保存登录状态
            if request.POST['remember'] == 'on':
                resp.set_cookie('uid', old_user.id, 3600 * 24 * 7)
                resp.set_cookie('username', old_user.username, 3600 * 24 * 7)
        except Exception as e:

            return resp
        return resp


# ---------- 退出登录模块 -----------
def logout(request):
    # 删除session
    if 'username' in request.session:
        del request.session['username']
    if 'uid' in request.session:
        del request.session['uid']

    resp = HttpResponseRedirect('/user/login')
    # 删除cookies
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')

    return resp
