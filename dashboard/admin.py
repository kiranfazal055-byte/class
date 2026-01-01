from django.contrib import admin

# Optional: Change the title of the Django admin page
admin.site.site_header = "Classter College Management"
admin.site.site_title = "Classter Admin"
admin.site.index_title = "Welcome to Classter Administration"

# If you create any models in the dashboard app later, register them here
# Example:
# from .models import DashboardSetting
# admin.site.register(DashboardSetting)

# Currently, no models to register from dashboard app
# All main models (Student, Teacher, etc.) are registered in academics/admin.py