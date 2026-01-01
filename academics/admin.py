from django.contrib import admin
from .models import *

admin.site.register([Student, Teacher, Section, Exam, Mark, Session, Announcement])