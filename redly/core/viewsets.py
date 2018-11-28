from rest_framework import viewsets,filters
from .models import User
from .serializers import Usercad

class CadUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Usercad
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email', 'name')
