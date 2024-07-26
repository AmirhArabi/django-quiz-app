from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=150, unique=True, verbose_name='دسته بندی', null=False, blank=False)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Question(models.Model):
    CHOISES = [
        ('option1', 'option1'),
        ('option2', 'option2'),
        ('option3', 'option3'),
        ('option4', 'option4'),
    ]
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    question = models.CharField(max_length=50, unique=True, verbose_name='سوال')
    option1 = models.CharField(max_length=50, verbose_name='گزینه اول')
    option2 = models.CharField(max_length=50, verbose_name='گزینه دوم')
    option3 = models.CharField(max_length=50, verbose_name='گزینه سوم')
    option4 = models.CharField(max_length=50, verbose_name='گزینه چهارم')
    answer = models.CharField(max_length=7, choices=CHOISES, verbose_name='پاسخ', help_text='گزینه درست را انتخاب کنید')
    status = models.BooleanField(default=False, help_text='وضعیت انتشار سوال', verbose_name='وضعیت')
    image = models.ImageField(upload_to='images/', verbose_name='تصویر', blank=True, null=True,
                              help_text='تصویر مربوط به سوال', default='images/default.png')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'سوال'
        verbose_name_plural = 'سوال ها'


class UserResult(models.Model):
    username = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    total = models.PositiveSmallIntegerField(default=0, verbose_name='کل سوالات')
    score = models.PositiveSmallIntegerField(default=0, verbose_name='امتیاز')
    percent = models.FloatField(max_length=5, verbose_name='درصد')
    current = models.PositiveSmallIntegerField(default=0, verbose_name='تعداد سوالات درست')
    wrong = models.PositiveSmallIntegerField(default=0, verbose_name='تعداد سوالات غلط')
    last_update = models.DateTimeField(auto_now_add=True, verbose_name='آخرین تغییر ', blank=True, null=True)

    def __str__(self):
        return self.username.username

    class Meta:
        verbose_name = 'نتیجه'
        verbose_name_plural = 'نتایج'
