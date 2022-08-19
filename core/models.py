from django.db import models

# ---------------------------------------------------------------------------- #
#                         //! Create your models here.                         #
# ---------------------------------------------------------------------------- #


#@ User accounts
class UserAcc(models.Model):
    email = models.CharField(max_length=256,default="no value")
    number = models.IntegerField(default=1)
    password = models.CharField(max_length=50,default="no value") 

    class Meta:
        ordering = ['id']



#@ Admin Accounts
class AdminAcc(models.Model):
    email = models.CharField(max_length=256,default="no value")
    number = models.IntegerField(default=1)
    password = models.CharField(max_length=20,default="no value")  

    companyName = models.CharField(max_length=100,default="no value")  
    proofOfBiz_link = models.CharField(max_length=500,default="no value")  
    category = models.CharField(max_length=40,default="no value")  

    loc_firstLine = models.CharField(max_length=200,default="no value")  
    loc_secondLine = models.CharField(max_length=200,default="no value")  
    loc_pincode = models.IntegerField(default=1)

    isAgreementAccpeted = models.BooleanField(default=False)
    isAdminVerified = models.BooleanField(default=False) # to turn to true by superAdmin
    # maxQueueNumber = models.IntegerField(default=0)  # let each admin create only 5 queues


    class Meta:
        ordering = ['id']




#@ Queue DB
class Queue(models.Model):
    adminAcc_fk = models.ForeignKey(AdminAcc,blank=True, null=True, on_delete=models.CASCADE,related_name='adminAccFk_in_queue')
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=80)
    setMaxPeople =  models.IntegerField(default=1000)  # people cant join anymore, if this num exists
    isOpen = models.BooleanField(default=True)  # bool to open/close queues on holidays etc

    class Meta:
        ordering = ['id']




#@ QueueUser DB
class QueueUser(models.Model):
    # this user joined which queue number
    queue_fk = models.ForeignKey(Queue,blank=True, null=True, on_delete=models.CASCADE, related_name='queueFk_in_queueUser') 
    queue_name = models.CharField(max_length=80,default='no value')

    # which user joined this queue
    userAcc_fk = models.ForeignKey(UserAcc,blank=True, null=True,on_delete=models.CASCADE, related_name='userAccFk_in_queueUser') 
    userAcc_name = models.CharField(max_length=80,default='no value')

    # user joined queue of which admin (shop)
    adminAcc_fk = models.ForeignKey(AdminAcc,blank=True, null=True,on_delete=models.CASCADE, related_name='adminAccFk_in_queueUser') 
    adminAcc_name = models.CharField(max_length=80,default='no value')
    
    joinedTime = models.CharField(max_length=50)  

    class Meta:
        ordering = ['id']


