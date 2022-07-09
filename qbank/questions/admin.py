from django.contrib import admin
from .models import Question

class QBankAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
# Register your models here.
admin.site.register(Question, QBankAdmin)
