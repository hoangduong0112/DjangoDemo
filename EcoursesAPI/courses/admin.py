from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin

# Register your models here.
# from EcoursesAPI.courses.models import category ERROR
from .models import category, Tag, Lesson
from .models import Course
from django.utils.html import mark_safe

class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Course
        fields = '__all__'

class LessonInlineAdmin(admin.StackedInline):
    model = Lesson
    fk_name = 'course'

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date', 'active']
    search_fields = ['name', 'description']
    list_filter = ['id', 'name', 'created_date']
    readonly_fields = ['my_image']
    form = CourseForm
    inlines = [LessonInlineAdmin, ]

    def my_image(self, course):
        if course.image:
            return mark_safe(f"<image width='200' src='{course.image.url}'/>")

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }

admin.site.register(category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Tag)
admin.site.register(Lesson)