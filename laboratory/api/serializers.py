from rest_framework.serializers import ModelSerializer

from reagents.models import Reagent


class ReagentSerializer(ModelSerializer):
    class Meta:
        model = Reagent
        fields = ['id', 'index', 'name', 'grade', 'amount',
                  'manufacture_date', 'expiration_date']
        ordering = ['index']
