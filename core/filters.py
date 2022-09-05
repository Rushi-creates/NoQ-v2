import django_filters
from .models import * 

class UserAccFilters(django_filters.FilterSet):
    class Meta: 
        model = UserAcc
        fields = '__all__'

class AdminAccFilters(django_filters.FilterSet):
    class Meta: 
        model = AdminAcc
        fields = '__all__'

class QueueFilters(django_filters.FilterSet):
    class Meta: 
        model = Queue
        # fields = '__all__'
        fields = ['id','name','description','setMaxPeople','isOpen','adminAcc_fk']

class QueueUserFilters(django_filters.FilterSet):
    class Meta: 
        model = QueueUser
        fields = '__all__'

