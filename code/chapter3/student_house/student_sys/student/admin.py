from django.contrib import admin
# Register your models here.
from student.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'profession', 'email', 'qq', 'phone', 'status', 'created_time')
    list_filter = ('sex', 'status', 'created_time')
    fieldsets = (
        (None, {
            'fields':(
                'name',
                ('sex', 'profession'),
                ('email', 'qq', 'phone'),
                'status'
            )
        }),
    )


admin.site.register(Student, StudentAdmin)