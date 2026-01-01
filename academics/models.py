from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)

class Section(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(Student)

class Exam(models.Model):
    name = models.CharField(max_length=200)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    total_marks = models.IntegerField(default=100)

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()

class Session(models.Model):
    title = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()
    color = models.CharField(max_length=20)

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()