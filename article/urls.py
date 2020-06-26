from django.urls import path
from . import views
from .views import MessageView

app_name = 'article'

urlpatterns = [
    path('', views.message_list, name='message_list'),
    path('add/', views.add_message, name='add_message'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('messages/', MessageView.as_view()),
    path('messages/<int:pk>', MessageView.as_view())
]