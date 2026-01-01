from django import forms
from .models import Student, Teacher, Section, Exam, Announcement, Mark  # Add Mark here

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = '__all__'

# ← Add this new form
class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = '__all__'