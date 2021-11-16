from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import Note


# Create your views here.

def login_check(func):
    def wrap(request, *args, **kwargs):

        # 检查session
        if 'username' not in request.session and 'uid' not in request.session:
            username_cookies = request.COOKIES.get('username')
            uid_cookies = request.COOKIES.get('uid')

            # 检查cookies
            if not username_cookies or not uid_cookies:
                return HttpResponseRedirect('/user/login')
            else:
                # 回写session
                request.session['username'] = username_cookies
                request.session['uid'] = uid_cookies

        return func(request, *args, **kwargs)

    return wrap


@login_check
def add_view(request):

    if request.method == "GET":
        return render(request, 'note/add_note.html')

    elif request.method == "POST":

        title = request.POST['title']
        content = request.POST['content']
        uid = request.session['uid']
        Note.objects.create(title=title, content=content, user_id=uid)
        return HttpResponse('添加笔记成功！')
