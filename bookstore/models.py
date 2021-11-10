from django.db import models


# Create your models here.


class Book(models.Model):
    title = models.CharField("书名", max_length=50, default='')
    price = models.DecimalField("定价", max_digits=5, decimal_places=2, default=0.0)

    market_price = models.DecimalField('市场价', max_digits=5, decimal_places=2, default=0.0)
    publish = models.CharField('出版社', max_length=50, default='')
    is_active = models.BooleanField('是否活跃', default=True)

    def __str__(self):
        return f'书名：{self.title} 定价:{self.price} 市场价:{self.market_price} 出版社{self.publish}'

    class Meta:
        db_table = 'books'
        verbose_name = '图书列表'
        verbose_name_plural = '图书列表'


class Author(models.Model):
    name = models.CharField('姓名', max_length=20)
    age = models.IntegerField('年龄', default=19)
    email = models.EmailField('邮箱', null=True)

    class Meta:
        # db_table = 'books'
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
