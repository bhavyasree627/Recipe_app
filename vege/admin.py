from django.contrib import admin
from django.db.models import Sum
# Register your models here.

from .models import *

admin.site.register(Receipe)

admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Subject)

class SubjectMarkAdmin(admin.ModelAdmin):
    list_display=['student','subject','marks']

admin.site.register(SubjectMarks,SubjectMarkAdmin)

# class ReportCardAdmin(admin.ModelAdmin):
#     list_display=['student','student_rank','total_marks','date_of_report_card_generation']
#     def total_marks(self,obj):
#         subject_marks=Subjects.objects.filter(student=obj.student)
#         return obj.aggregate(marks=Sum('marks'))

# admin.site.register(ReportCard,ReportCardAdmin)