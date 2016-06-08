from nuggetsapp.models import Nugget
from rest_framework import serializers


class NuggetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nugget
        fields = ('owner_name', 'source', 'text', 'url', 'tags', 'created_at', 'updated_at', 'is_deleted')
