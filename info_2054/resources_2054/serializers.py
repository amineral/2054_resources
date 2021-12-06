from rest_framework import serializers
from .models import Computer, InteractiveBoard

class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ['comp_type', 'brand', 'serial_number', 'owner', 'status', 'dp']

class InteractiveBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractiveBoard
        fields = '__all__'

