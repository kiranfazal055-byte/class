from django.urls import path
from .views import dashboard, calendar_events, chart_data

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('calendar-events/', calendar_events),
    path('chart-data/', chart_data),
]