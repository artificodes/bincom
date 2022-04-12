from rest_framework import serializers
from .models import *



class PollingUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollingUnit
        fields = '__all__'


class AnnouncedPollingUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncedPuResults
        fields = '__all__'

class LGAsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lga
        fields = '__all__'