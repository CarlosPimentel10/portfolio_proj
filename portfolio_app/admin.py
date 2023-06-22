from django.contrib import admin
from .models import CustomUser, UserProfile
from django.urls import reverse
from auditlog.models import AuditlogHistory



class AuditlogHistoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'timestamp', 'action']
    
admin.site.register(CustomUser)
admin.site.register(AuditlogHistory, AuditlogHistoryAdmin)


