from django.contrib import admin
import clients.models as models


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'telegram', 'problem_client')
