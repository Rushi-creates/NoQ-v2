from rest_framework import serializers
from core.models import *



class QueueSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Queue
        fields = '__all__'


class QueueUserSerializer(serializers.ModelSerializer):
    class Meta : 
        model = QueueUser
        fields = '__all__'


class UserAccSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAcc
        fields = '__all__'


class AdminAccSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminAcc
        fields = '__all__'

