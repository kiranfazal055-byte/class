from django.shortcuts import render
from django.http import JsonResponse
from academics.models import Student, Teacher, Section, Session, Announcement, Mark

def dashboard(request):
    context = {
        'students_count': Student.objects.count(),
        'teachers_count': Teacher.objects.count(),
        'sections_count': Section.objects.count(),
        'announcements': Announcement.objects.all(),
    }
    return render(request, 'dashboard/dashboard.html', context)

def calendar_events(request):
    events = list(Session.objects.values('title', 'start', 'end', 'color'))
    return JsonResponse(events, safe=False)

def chart_data(request):
    # Sample; customize with real data
    data = {
        'absence_bar': {'labels': ['Year 1', 'Year 2'], 'data': [35, 25]},
        'attendance_line': {'labels': ['Jan', 'Feb'], 'data': [90, 85]},
        'gender_pie': {'labels': ['Male', 'Female'], 'data': [60, 40]},
    }
    return JsonResponse(data)