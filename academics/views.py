from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin  # Optional: add later for security
from .models import (
    Student, Teacher, Section, Exam, Mark, Session, Announcement
)
from .forms import (
    StudentForm, TeacherForm, SectionForm, ExamForm, MarkForm, AnnouncementForm
)
from django.db.models import Avg, Sum

# -------------------------- Students --------------------------
class StudentListView(ListView):
    model = Student
    template_name = 'academics/student_list.html'
    context_object_name = 'students'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'academics/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'academics/student_form.html'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'academics/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')

# -------------------------- Teachers --------------------------
class TeacherListView(ListView):
    model = Teacher
    template_name = 'academics/teacher_list.html'
    context_object_name = 'teachers'

class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'academics/teacher_form.html'
    success_url = reverse_lazy('teacher_list')

class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'academics/teacher_form.html'
    success_url = reverse_lazy('teacher_list')

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'academics/teacher_confirm_delete.html'
    success_url = reverse_lazy('teacher_list')

# -------------------------- Sections --------------------------
class SectionListView(ListView):
    model = Section
    template_name = 'academics/section_list.html'
    context_object_name = 'sections'

class SectionCreateView(CreateView):
    model = Section
    form_class = SectionForm
    template_name = 'academics/section_form.html'
    success_url = reverse_lazy('section_list')

class SectionUpdateView(UpdateView):
    model = Section
    form_class = SectionForm
    template_name = 'academics/section_form.html'
    success_url = reverse_lazy('section_list')

# -------------------------- Exams & Quizzes --------------------------
class ExamListView(ListView):
    model = Exam
    template_name = 'academics/exam_list.html'
    context_object_name = 'exams'

class ExamCreateView(CreateView):
    model = Exam
    form_class = ExamForm
    template_name = 'academics/exam_form.html'
    success_url = reverse_lazy('exam_list')

# -------------------------- Marks Entry --------------------------
def marks_entry(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    students = exam.section.students.all() if hasattr(exam, 'section') else Student.objects.all()

    if request.method == 'POST':
        for student in students:
            marks_key = f'marks_{student.id}'
            if marks_key in request.POST:
                marks_obtained = request.POST[marks_key]
                if marks_obtained:
                    Mark.objects.update_or_create(
                        student=student,
                        exam=exam,
                        defaults={'marks_obtained': marks_obtained}
                    )
        return redirect('exam_list')

    return render(request, 'academics/marks_entry.html', {
        'exam': exam,
        'students': students,
    })

# -------------------------- Report Cards --------------------------
def report_card(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    marks = Mark.objects.filter(student=student)

    total_obtained = marks.aggregate(Sum('marks_obtained'))['marks_obtained__sum'] or 0
    total_possible = marks.aggregate(Sum('exam__total_marks'))['exam__total_marks__sum'] or 1
    percentage = (total_obtained / total_possible) * 100 if total_possible else 0

    context = {
        'student': student,
        'marks': marks,
        'percentage': round(percentage, 2),
        'grade': 'A+' if percentage >= 90 else 'A' if percentage >= 80 else 'B' if percentage >= 70 else 'C' if percentage >= 60 else 'F',
    }
    return render(request, 'academics/report_card.html', context)

# -------------------------- Announcements --------------------------
class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'academics/announcement_list.html'
    context_object_name = 'announcements'
    ordering = ['-id']

class AnnouncementCreateView(CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'academics/announcement_form.html'
    success_url = reverse_lazy('announcement_list')