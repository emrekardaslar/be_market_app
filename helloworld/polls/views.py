from rest_framework import viewsets
from rest_framework import permissions
from .models import Question

from .serializers import PollsSerializer


class QuestionsSerializerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all().order_by('pub_date')
    serializer_class = PollsSerializer
    permission_classes = [permissions.IsAuthenticated]