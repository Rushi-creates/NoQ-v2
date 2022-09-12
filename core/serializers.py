from rest_framework import serializers
from core.models import *



class QueueSerializer(serializers.ModelSerializer):
    totalPeople = serializers.SerializerMethodField('get_totalPeople')

    class Meta : 
        model = Queue
        # fields = '__all__'
        fields = ['id','name','description','setMaxPeople','isOpen','adminAcc_fk','totalPeople']

    def get_totalPeople(self, singleObj):
        getId = getattr(singleObj, 'id')  #! _id is imp
        count = QueueUser.objects.filter(queue_fk=getId).count()
        return count







class QueueUserSerializer(serializers.ModelSerializer):
    queue_name = serializers.SerializerMethodField('get_queueName')
    userAcc_name = serializers.SerializerMethodField('get_userAccName')
    adminAcc_name = serializers.SerializerMethodField('get_adminAcc_name')
    queueCount = serializers.SerializerMethodField('get_queueCount')
    myTurn = serializers.SerializerMethodField('get_myTurn')


    # def get_queueCount(self, singleObj):   # old
    #     getQueueFk = getattr(singleObj, 'queue_fk_id')  #! _id is imp
    #     storeObj = Queue.objects.get(id=getQueueFk)
    #     serializer = QueueSerializer(instance=storeObj)
    #     return serializer.data['totalPeople']

    def get_adminAcc_name(self, singleObj): 
        getadminAccFk = getattr(singleObj, 'adminAcc_fk_id')  #! _id is imp
        adminAccObj = AdminAcc.objects.get(id=getadminAccFk)
        serializer = AdminAccSerializer(instance=adminAccObj)
        return serializer.data["companyName"]

    def get_userAccName(self, singleObj): 
        getUserAccFk = getattr(singleObj, 'userAcc_fk_id')  #! _id is imp
        userAccObj = UserAcc.objects.get(id=getUserAccFk)
        serializer = UserAccSerializer(instance=userAccObj)
        return serializer.data["email"]

    def get_queueName(self, singleObj): 
        getQueueFk = getattr(singleObj, 'queue_fk_id')  #! _id is imp
        queueObj = Queue.objects.get(id=getQueueFk)
        serializer = QueueSerializer(instance=queueObj)
        return serializer.data["name"]

    def get_queueCount(self, singleObj): 
        getQueueFk = getattr(singleObj, 'queue_fk_id')  #! _id is imp
        count = QueueUser.objects.filter(queue_fk=getQueueFk).count()
        return count

    def get_myTurn(self, singleObj): 
        getQueueFk = getattr(singleObj, 'queue_fk_id')  #! _id is imp
        getId = getattr(singleObj, 'id')
        count = QueueUser.objects.filter(queue_fk=getQueueFk).filter(pk__lte = getId).count()
        return count


    class Meta : 
        model = QueueUser
        # fields = '__all__'
        fields = [
            'id',
            'queue_fk',
            'queue_name',
            'userAcc_fk',
            'userAcc_name',
            'adminAcc_fk',
            'adminAcc_name',
            'joinedTime',
            'queueCount','myTurn'
        ]




class UserAccSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAcc
        fields = '__all__'


class AdminAccSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminAcc
        fields = '__all__'

