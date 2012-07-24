from result.models import *

from django.contrib import admin

#class resultdisp(admin.ModelAdmin):
#    list_display = ('branch')
class grade_disp(admin.ModelAdmin):
    list_display = ('student','subject','student_dep','maximum_marks','marks_obtained')

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(StudentDep)
admin.site.register(Exam,grade_disp)