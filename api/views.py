from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.serializers import ReagentSerializer
from reagents.models import Reagent


class ReagentViewSet(ModelViewSet):
    queryset = Reagent.objects.all()
    serializer_class = ReagentSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']
    filter_backends = [SearchFilter]
    search_fields = ['name']
