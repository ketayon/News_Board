from django.contrib import admin

from .models import Message, Comment

# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'creation_date', 'amount_of_upvotes','author_name')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('message', 'name', 'body', 'created')