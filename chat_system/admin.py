from django.contrib import admin
from .models import MessageContent, Messages


class MessageContentAdmin(admin.ModelAdmin):
    list_display = ('content', 'timestamp', 'superuser')
    list_filter = ('superuser', 'timestamp')
    search_fields = ('content',)


admin.site.register(MessageContent, MessageContentAdmin)


class MessagesAdmin(admin.ModelAdmin):
    list_display = ('sender', 'timestamp', 'product')
    list_filter = ('timestamp', 'product')
    search_fields = ('sender__username', 'product__name')


admin.site.register(Messages, MessagesAdmin)
