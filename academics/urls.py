from django.urls import path
from .views import *

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/add/', StudentCreateView.as_view(), name='student_add'),
    path('students/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_edit'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),

    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teachers/add/', TeacherCreateView.as_view(), name='teacher_add'),

    path('sections/', SectionListView.as_view(), name='section_list'),
    path('sections/add/', SectionCreateView.as_view(), name='section_add'),

    path('exams/', ExamListView.as_view(), name='exam_list'),
    path('exams/add/', ExamCreateView.as_view(), name='exam_add'),
    path('exams/<int:exam_id>/marks/', marks_entry, name='marks_entry'),

    path('report/<int:student_id>/', report_card, name='report_card'),

    path('announcements/', AnnouncementListView.as_view(), name='announcement_list'),
    path('announcements/add/', AnnouncementCreateView.as_view(), name='announcement_add'),
]