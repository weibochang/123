from django.shortcuts import render,redirect
from .models import BlogUser,EmailVerifyRecord
import hashlib
from .form import UserForm,RegisterForm
from django.contrib.auth.hashers import make_password, check_password


def login(request):
    if request.session.get('is_login',None):
        return redirect('/blog/index/')
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        if login_form.is_valid():
            msg = '所有字段都必须填写'
            print(msg)
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user=BlogUser.objects.get(username=username)

                if check_password(password,user.password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return redirect('/blog/index/')
                else:
                    msg = '密码错误，请核对密码后重试'
            except:
                msg='用户名不存在'
        return render(request,'login.html',locals())
        # python中内容了一个local()函数，它返回当前多有的本地变量的字典，可以使用local()传输到前端数据，但是，
        # 它有一点不好，就是会把所有的变量和对应值传过去，造成了数据的冗余
    else:
        login_form = UserForm()
        return render(request,'login.html',locals())
def register(request):
    if request.session.get('is_login',None):
        return redirect('/blog/index/')
    if request.method == 'POST':
        msg = '请填写所有字段的内容'
        print(msg)
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():

            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password2 != password1:
                msg='两次输入的密码不一致！'
                return render(request,'register.html',locals())
            else:
                all_uname = BlogUser.objects.filter(username=username)
                if all_uname:
                    msg='该用户名已被使用，请重新选择用户名！'
                    return render(request,'register.html',locals())
                all_uemail = BlogUser.objects.filter(email=email)
                if all_uemail:
                    msg='该邮箱号已经被注册，请使用其他邮箱'
                    return render(request, 'register.html', locals())
                new_user = BlogUser()
                print(1234123412341234123412341234)
                new_user.username = username
                new_user.email=email
                new_user.sex=sex
                new_user.password=make_password(password1)
                # new_user.
                new_user.save()
                return redirect('/user/login/')
        return render(request, 'register.html', locals())
    register_form = RegisterForm()
    return render(request,'register.html',locals())
def logout(request):
    # print(request.session.get('is_login',None))
    if not request.session.get('is_login',None):
        return redirect('/blog/index/')
    request.session.flush()
    print('123')
    return redirect('/blog/index/')