from django.contrib import admin
from .models import CustomUser
from auditlog.models import LogEntry


class AuditlogHistoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'get_username', 'timestamp', 'action']

    def get_username(self, obj):
        return obj.user.username if obj.user else None
    get_username.short_description = 'Username'

# UNREGISTER LOGENTRY TO AVOID DB CONFLICT
admin.site.unregister(LogEntry)
admin.site.register(LogEntry, AuditlogHistoryAdmin)
admin.site.register(CustomUser)
