from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Message
from .forms import AddMessageForm, CommentForm
from .serializers import MessageSerializer
# Create your views here.

def message_list(request):
    messages = Message.objects.all()
    return render(request, 'article/message/list.html', {'messages': messages})

def add_message(request):
        form = AddMessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/article/')
        return render(request, 'article/message/add.html', {'form': form})

def add_comment(request):
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/article/')
        return render(request, 'article/message/add_comment.html', {'form': form})

class MessageView(APIView):
    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response({"messages": serializer.data})

    def post(self, request):
        message = request.data.get('message')
        serializer = MessageSerializer(data=message)
        if serializer.is_valid(raise_exception=True):
            message_saved = serializer.save()
        return Response({"success": "Message '{}' created successfully".format(message_saved.title)})

    def put(self, request, pk):
        saved_message = get_object_or_404(Message.objects.all(), pk=pk)
        data = request.data.get('message')
        serializer = MessageSerializer(instance=saved_message, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            message_saved = serializer.save()
        return Response({
            "success": "Message '{}' updated successfully".format(message_saved.title)
        })

    def delete(self, request, pk):
        message = get_object_or_404(Message.objects.all(), pk=pk)
        message.delete()
        return Response({
            "message": "Message with id `{}` has been deleted.".format(pk)
        }, status=204)