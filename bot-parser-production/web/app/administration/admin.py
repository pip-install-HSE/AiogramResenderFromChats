from django.contrib import admin

from .models import User, Message, Word, File, ChatMessage


class UserAdmin(admin.ModelAdmin):
	readonly_fields = ['id', 'name', 'lastname', 'username', 'created_at', 'updated_at']


class WordAdmin(admin.ModelAdmin):
	readonly_fields = ['user', 'search_words', 'stop_words']


class FileAdmin(admin.ModelAdmin):
	readonly_fields = ['file_name', 'file_id']


class MessageAdmin(admin.ModelAdmin):
	pass

class ChatMessageAdmin(admin.ModelAdmin):
	pass

admin.site.register(User, UserAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(ChatMessage, ChatMessageAdmin)
