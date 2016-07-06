from nuggetsapp.models import Nugget
from rest_framework import serializers


class NuggetSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if len(data['text']) > Nugget.MAX_TEXT_SIZE:
            raise serializers.ValidationError("Nugget text larger than 200 limit")
        return data

    class Meta:
        model = Nugget
        fields = ('id', 'owner_name', 'source', 'text', 'url', 'tags', 'created_at', 'updated_at', 'is_deleted')
