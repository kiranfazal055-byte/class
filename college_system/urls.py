from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),                  # Django admin panel (keep this)
    path('', include('dashboard.urls')),              # Your Classter dashboard at home page (/)
    path('academics/', include('academics.urls')),    # All student/teacher/exam pages under /academics/
]