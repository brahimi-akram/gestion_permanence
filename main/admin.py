from django.contrib import admin
from .models import *
admin.site.register(Permanence)
admin.site.register(Cadre)
admin.site.register(Affectation)

@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('objet','corpse')
    # Prevent adding new templates by hiding the 'Add' button
    def has_add_permission(self, request):
        return not Mail.objects.exists()

    # Optionally, restrict deletion as well
    def has_delete_permission(self, request, obj=None):
        return False
# Register your models here.
