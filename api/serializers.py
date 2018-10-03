# from rest_framework_json_api import serializers
from rest_framework import serializers
from .models import *


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = [
            'id',
            'name',
            'done',
            'mark',
            'deadline',
            'rate',
            'created',
            'updated',
            'completed',
        ]


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'
