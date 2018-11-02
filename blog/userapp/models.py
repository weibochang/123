from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#用自己的模型 替换掉 系统默认的模型
class BlogUser(AbstractUser):
    nickname = models.CharField('昵称',default='',max_length=128)
    sex = models.CharField('性别',max_length=10,default='')
class EmailVerifyRecord(models.Model):
    code =models.CharField('验证码',max_length=50,default='')
    email = models.EmailField(max_length=50,verbose_name='邮箱')
    send_type = models.CharField('验证码类型',choices=(('register','注册'),('forget','忘记密码'),('update_emial','忘记邮箱')),max_length=100)
    send_time = models.DateTimeField('发送时间',auto_now=True)
    class Meta:
        verbose_name='邮箱验证码'
        verbose_name_plural=verbose_name
    def __str__(self):
        return '{}{}'.format(self.email,self.code)


