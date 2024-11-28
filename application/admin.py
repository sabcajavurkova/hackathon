from django.contrib import admin

from .models import Student, Teacher, Lecture

class LectureInline(admin.TabularInline):
    model = Lecture
    extra = 0
    
class LecturesInline(admin.TabularInline):
    model = Lecture.students.through
    extra = 0

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    inlines = [LecturesInline]
    
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    inlines = [LectureInline]
    
class LectureAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')

admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Lecture, LectureAdmin)
