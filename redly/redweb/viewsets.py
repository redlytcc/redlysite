from rest_framework import viewsets,filters
from .models import Chat
from .serializers import Chatptgt

class ChatSend(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = Chatptgt
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nome','text','date','img')
