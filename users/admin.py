from django.contrib import admin
from .models import InviteUrl


class InviteUrlAdmin(admin.ModelAdmin):
    list_display = [field.name for field in InviteUrl._meta.fields]

    class Meta:
        model = InviteUrl


admin.site.register(InviteUrl, InviteUrlAdmin)
