from django.contrib import admin
import orders.models as models


class SubTaskInline(admin.StackedInline):
    model = models.SubTask
    extra = 1


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'closed', 'payed', 'deadline', 'status')
    inlines = (SubTaskInline, )
    search_fields = ('id', 'title', 'client', 'status')


@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('__str__', )