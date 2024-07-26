from django.contrib import admin
from .models import Question, UserResult, Category
from django.contrib.auth.models import Group


class ResultAdmin(admin.ModelAdmin):
    readonly_fields = (
        'username',
        'total',
        'score',
        'percent',
        'current',
        'wrong',
        'last_update',
    )
    list_display = ('username', 'percent', 'score', 'total')
    list_filter = ('percent',)
    search_fields = ('fullname',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'status', 'category')
    list_filter = ('status', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(UserResult, ResultAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.unregister(Group)
