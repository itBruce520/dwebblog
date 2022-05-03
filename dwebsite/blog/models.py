from django.db import models
from django.contrib.auth.models import User


# 用户信息
class Userinfo(models.Model):
    headImg = models.ImageField()
    nickName = models.CharField()
    belong = models.OneToOneField(User)  # 一对一关系

    def __int__(self):
        return self.id


# 文章分类
class Category(models.Model):
    name = models.CharField()
    belong = models.ForeignKey(self)  # 树形结构，递归

    def __int__(self):
        return self.id


# 文章
class Article(models.Model):
    title = models.CharField()
    cover = models.CharField()  # 这里的封面，存储的是图片的路径
    text = models.TextField()
    belong = models.ForeignKey(Userinfo)  # 一对多关系

    def __int__(self):
        return self.id


# 收藏
class Favourite(models.Model):
    belong_user = models.ForeignKey(Userinfo)
    belong_art = models.ForeignKey(Article)

    def __int__(self):
        return self.id


# 点赞
class Like(models.Model):
    belong_art = models.ForeignKey(Article)
    # num = models.IntegerField()
    belong_user = models.ForeignKey(Userinfo)

    def __int__(self):
        return self.id


# 打赏
class PayOrder(models.Model):
    order = models.CharField()
    price = models.CharField()
    status = models.BooleanField()

    def __int__(self):
        return self.id
