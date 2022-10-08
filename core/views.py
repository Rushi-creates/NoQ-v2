# from appNameFolder.fileName import func/className
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import UserAcc,AdminAcc, Queue,QueueUser
from core.myPaginations import MyCustomPagination
from core.serializers import  UserAccSerializer,AdminAccSerializer,QueueSerializer,QueueUserSerializer
from .filters import UserAccFilters,AdminAccFilters,QueueUserFilters , QueueFilters


import random
from django.core.mail import EmailMessage
from django.conf import settings



#! Create your views here.


# ---------------------------------------------------------------------------- #
#                                //! superadmin                                #
# ---------------------------------------------------------------------------- #

@api_view(['POST'])
def checkSuperAdmin(request):

    superString =request.data.get('superString')

    if superString == 'mango@gmail.com':
        return Response(True)
    else : 
        return Response(False)



# ---------------------------------------------------------------------------- #
#                                  //! UserAcc                                 #
# ---------------------------------------------------------------------------- #



@api_view(['GET'])
def getAll_UserAcc(request):
    paginator = MyCustomPagination()
    userObj = UserAcc.objects.all()
    filteredData = UserAccFilters(request.GET, queryset = userObj).qs # gives filter search options from filters.py
    try :
        context = paginator.paginate_queryset(filteredData, request)
        serializer = UserAccSerializer(context,many=True)
        return Response(serializer.data)
    except:
        return Response([])



@api_view(['GET'])
def getSingle_UserAcc(request,id):
    userObj = UserAcc.objects.get(id=id)
    serializer = UserAccSerializer(instance=userObj)
    return Response(serializer.data)


# call directly after otp is verified ( from frontend send email , pass)
@api_view(['POST'])
def register_UserAcc(request):
    userObj = UserAccSerializer(data=request.data)
    print(userObj)
    if userObj.is_valid():
        print('saved')
        userObj.save()
    return Response(userObj.data)


@api_view(['PUT'])
def update_UserAcc(request,id):
    userObj = UserAcc.objects.get(id=id)
    serializers = UserAccSerializer(instance=userObj, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)


@api_view(['DELETE' , 'GET'])
def delete_UserAcc(request,id):
    userObj = UserAcc.objects.get(id=id)
    userObj.delete()
    return Response(f"Deleted {id}")





# use before register button
@api_view(['POST'])
def verify_UserEmail_beforeRegister(request):


    myemail =request.data.get('email')
    mypass = request.data.get('password')

    # if acc exists, ask him to login
    if UserAcc.objects.filter(email=myemail).exists() and UserAcc.objects.filter(password= mypass).exists() :
        return Response('Account already exists, try to login') 

    # send otp, before registering 
    else:
        otp=random.randint(1000,9999) 
        print (otp)

        emailBody = 'Your OTP is : '+ str(otp) +'.\n'
        'if you think this was sent to you by mistake , please ignore this email'


        #note first send this same otp to some sms paid service with twillio  or to EMAIL (twillio  OR email code here)
        email = EmailMessage(
            'Verify your email :', # subject     
            emailBody,        # body 
            settings.EMAIL_HOST_USER,  # sender's email from settigs.py 
            [myemail],    # whom to send email 
            )
        email.fail_silently=False
        email.send()                 # actually send email


        # then send same otp to client
        return Response(otp)




# use before forgot password(update acc) button
@api_view(['POST'])
def forgotPasword_userAcc(request):

    

    myemail =request.data.get('email')


    # if account exists in DB, then only he can reset password
    if UserAcc.objects.filter(email=myemail).exists() :
        otp=random.randint(1000,9999) 
        print (otp)

        emailBody = 'Your OTP to reset password is '+ str(otp) +'.\n'
        'if you think this was sent to you by mistake , please ignore this email'

        # note first send this same otp to some sms paid service with twillio  or to EMAIL
        # twillio  OR email code here
        email = EmailMessage(
            'Verify your email :',                   # subject test here 
            emailBody,        # body text here 
            settings.EMAIL_HOST_USER,    # sender's email from settigs.py 
            [myemail],    # whom to send email 
            )
        email.fail_silently=False  # will sent us email notifying in case of any error
        email.send()                 # actually send email


        # then send same otp to client
        return Response(otp)

        # if email doesnt exist in DB , you cannot reset password
    else:
        return Response("This account email doesn't exists, please enter right email, or create account first")  




@api_view(['POST'])
def login_UserAcc(request):

    # using get() method of py dict(to access value, by using the key), and store it in var
    myemail =request.data.get('email')
    mypass = request.data.get('password')

    # if email,pass exists in DB, then return full userAccObj
    if UserAcc.objects.filter(email=myemail).exists() and UserAcc.objects.filter(password= mypass).exists() : 
        userObj = UserAcc.objects.get(email=myemail, password =mypass)
        serializer = UserAccSerializer(instance=userObj)
        return Response(serializer.data)

    # if email and pass wrong/doesnt exists in DB 
    else:
        return Response("This account doesn't exist, enter correct details or try to register.")  




# ---------------------------------------------------------------------------- #
#                                 //! AdminAcc                                 #
# ---------------------------------------------------------------------------- #



@api_view(['GET'])
def getAll_AdminAcc(request):
    paginator = MyCustomPagination()
    userObj = AdminAcc.objects.all()
    filteredData = AdminAccFilters(request.GET, queryset = userObj).qs # gives filter search options from filters.py
    try :
        context = paginator.paginate_queryset(filteredData, request)
        serializer = AdminAccSerializer(context,many=True)
        return Response(serializer.data)
    except:
        return Response([])




#! let user search adminsAcc by emails  in search field 
@api_view(['GET'])
def get_regex_AdminAcc(request):

    paginator = MyCustomPagination()
    filteredData = AdminAcc.objects.filter(email__icontains=request.GET['email'])
    try :
        context = paginator.paginate_queryset(filteredData, request)
        serializer = AdminAccSerializer(context,many=True)
        return Response(serializer.data)
    except:
        return Response([])

#! let user search adminsAcc by emails  in search field 
@api_view(['GET'])
def get_regex_byCompanyName_AdminAcc(request):

    paginator = MyCustomPagination()
    filteredData = AdminAcc.objects.filter(companyName__icontains=request.GET['companyName'])
    try :
        context = paginator.paginate_queryset(filteredData, request)
        serializer = AdminAccSerializer(context,many=True)
        return Response(serializer.data)
    except:
        return Response([])




# #! let user search adminsAcc by emails  in search field 
# @api_view(['POST'])
# def get_regex_AdminAcc(request):

#     mySearch =request.data.get('searchData')

#     paginator = MyCustomPagination()
#     filteredData = AdminAcc.objects.filter(email__icontains=mySearch)
#     print(filteredData)
#     try :
#         context = paginator.paginate_queryset(filteredData, request)
#         serializer = AdminAccSerializer(context,many=True)
#         return Response(serializer.data)
#     except:
#         return Response([])



@api_view(['GET'])
def getSingle_AdminAcc(request,id):
    userObj = AdminAcc.objects.get(id=id)
    serializer = AdminAccSerializer(instance=userObj)
    return Response(serializer.data)


# call directly after otp is verified ( from frontend send email , pass)
@api_view(['POST'])
def register_AdminAcc(request):
    userObj = AdminAccSerializer(data=request.data)
    if userObj.is_valid():
        userObj.save()
    return Response(userObj.data)


@api_view(['PUT'])
def update_AdminAcc(request,id):
    userObj = AdminAcc.objects.get(id=id)
    serializers = AdminAccSerializer(instance=userObj, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)


@api_view(['DELETE' , 'GET'])
def delete_AdminAcc(request,id):
    userObj = AdminAcc.objects.get(id=id)
    userObj.delete()
    return Response(f"Deleted {id}")





# use before register button
@api_view(['POST'])
def verify_AdminEmail_beforeRegister(request):

  
    myemail =request.data.get('email')
    mypass = request.data.get('password')

    # if acc exisits, ask him to login
    if AdminAcc.objects.filter(email=myemail).exists() and AdminAcc.objects.filter(password= mypass).exists() :
        return Response('Account already exists, try to login') 

    # send otp, before registering 
    else:
        otp=random.randint(1000,9999) 
        print (otp)

        emailBody = 'Your OTP is : '+ str(otp) +'.\n'
        'if you think this was sent to you by mistake , please ignore this email'


        #note first send this same otp to some sms paid service with twillio  or to EMAIL (twillio  OR email code here)
        email = EmailMessage(
            'Verify your email :', # subject     
            emailBody,        # body 
            settings.EMAIL_HOST_USER,  # sender's email from settigs.py 
            [myemail],    # whom to send email 
            )
        email.fail_silently=False
        email.send()                 # actually send email


        # then send same otp to client
        return Response(otp)




# use before forgot password(update acc) button
@api_view(['POST'])
def forgotPasword_AdminAcc(request):

    emailBody = 'Your OTP to reset password is '+ str(otp) +'.\n'
    'if you think this was sent to you by mistake , please ignore this email'

    myemail =request.data.get('email')


    # if account exists in DB, then only he can reset password
    if AdminAcc.objects.filter(email=myemail).exists() :
        otp=random.randint(1000,9999) 
        print (otp)

        # note first send this same otp to some sms paid service with twillio  or to EMAIL
        # twillio  OR email code here
        email = EmailMessage(
            'Verify your email :',                   # subject test here 
            emailBody,        # body text here 
            settings.EMAIL_HOST_USER,    # sender's email from settigs.py 
            [myemail],    # whom to send email 
            )
        email.fail_silently=False  # will sent us email notifying in case of any error
        email.send()                 # actually send email


        # then send same otp to client
        return Response(otp)

        # if email doesnt exist in DB , you cannot reset password
    else:
        return Response("This account email doesn't exists, please enter right email, or create account first")  




@api_view(['POST'])
def login_AdminAcc(request):

    # using get() method of py dict(to access value, by using the key), and store it in var
    myemail =request.data.get('email')
    mypass = request.data.get('password')

    # if email,pass exists in DB, then return full userAccObj
    if AdminAcc.objects.filter(email=myemail).exists() and AdminAcc.objects.filter(password= mypass).exists() : 
        userObj = AdminAcc.objects.get(email=myemail, password =mypass)
        serializer = AdminAccSerializer(instance=userObj)
        return Response(serializer.data)

    # if email and pass wrong/doesnt exists in DB 
    else:
        return Response("This account doesn't exist, enter correct details or try to register")  








# ---------------------------------------------------------------------------- #
#                                //! Queue                                     #
# ---------------------------------------------------------------------------- #
@api_view(['POST'])
def addQueue(request):

    my_adminAcc_fk = request.data.get('adminAcc_fk')
    totalQueues = Queue.objects.filter(adminAcc_fk=my_adminAcc_fk).count()

    if totalQueues > 5:
         # each admin must be able to create only 5 queues
         # add subscription model to be able to create more than 5 queues
        return Response('Cant create more than 5 queues') 
    else:
        userObj = QueueSerializer(data=request.data)
        if userObj.is_valid():
            userObj.save()
        return Response(userObj.data)



@api_view(['GET'])
def getQueue(request):
    # get map of query params passed by user
    # print('=============' + str(request.GET))
    # print('=============' + str(request.GET['queue_fk'])) 
    paginator = MyCustomPagination()
    userObj = Queue.objects.all()

    ## get toal people 
    # totalPeople = QueueUser.objects.filter(queue_fk=request.GET['queue_fk']).count()
    # userObj.total_people = 

    # og from here
    filteredData = QueueFilters(request.GET, queryset = userObj).qs # gives filter search options from filters.py
    try :
        context = paginator.paginate_queryset(filteredData, request)
        serializer = QueueSerializer(context,many=True)
        return Response(serializer.data)
    except:
        return Response([])


@api_view(['GET'])
def getSingleQueue(request,id):
    userObj = Queue.objects.get(id=id)
    serializer = QueueSerializer(instance=userObj)
    return Response(serializer.data)

@api_view(['PUT'])
def updateQueue(request,id):
    userObj = Queue.objects.get(id=id)
    serializers = QueueSerializer(instance=userObj, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE' , 'GET'])
def deleteQueue(request,id):
    userObj = Queue.objects.get(id=id)  #! make sure to chaneg id , to g_uid here
    userObj.delete()
    return Response(f"Deleted {id}")


# dont need this here , as uid and id are the same 
@api_view(['DELETE' , 'GET'])
def deleteQueueByUid(request,uid):
    userObj = Queue.objects.get(g_uid=uid)  #! just changed uid here 
    userObj.delete()
    return Response(f"Deleted by uid {uid}")






# ---------------------------------------------------------------------------- #
#                                //! QueueUser                                 #
# ---------------------------------------------------------------------------- #


@api_view(['POST'])
def addQueueUser(request):
    my_userAcc_fk = request.data.get('userAcc_fk')
    my_queue_fk = request.data.get('queue_fk')
    my_adminAcc_fk = request.data.get('adminAcc_fk')
    

    # one queueUser per 'shop'
    if QueueUser.objects.filter(userAcc_fk=my_userAcc_fk,queue_fk=my_queue_fk,adminAcc_fk=my_adminAcc_fk).exists() :
        return Response("You have already joined 1 queue of this shop, can't join more")
    else:
        userObj = QueueUserSerializer(data=request.data)
        if userObj.is_valid():
            userObj.save()

            # #! Start- update queue DB totalPeople prop , when new queueUser added to that queue
            # totalPeopleCount = QueueUser.objects.filter(queue_fk=my_queue_fk).count()
            # myQueueObj = Queue.objects.get(id=my_queue_fk) # get single obj
            # # partial= true , is patch update ( thus imp )
            # qSerializer = QueueSerializer(instance=myQueueObj, data= {'totalPeople' : totalPeopleCount}, partial = True)
            
            # if qSerializer.is_valid():
            #     qSerializer.save()
            #     print(qSerializer.data)
            # #! end of queue DB modifictaion 

        return Response(userObj.data)
        



@api_view(['GET'])
def getQueueUser(request):
    paginator = MyCustomPagination()
    userObj = QueueUser.objects.all()
    filteredData = QueueUserFilters(request.GET, queryset = userObj).qs # gives filter search options from filters.py
    try :
        context = paginator.paginate_queryset(filteredData, request)
        serializer = QueueUserSerializer(context,many=True)
        return Response(serializer.data)
    except:
        return Response([])


@api_view(['GET'])
def getSingleQueueUser(request,id):
    userObj = QueueUser.objects.get(id=id)
    serializer = QueueUserSerializer(instance=userObj)
    return Response(serializer.data)

@api_view(['PUT'])
def updateQueueUser(request,id):
    userObj = QueueUser.objects.get(id=id)
    serializers = QueueUserSerializer(instance=userObj, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE' , 'GET'])
def deleteQueueUser(request,id):
    userObj = QueueUser.objects.get(id=id)  #! make sure to chaneg id , to g_uid here

    # getQueue_fk = userObj.queue_fk_id  #! _id at end is imp 
    userObj.delete()

    # # make sure to keep this after delete only
    # #! Start- update queue (not queueUser) DB totalPeople prop , when new queueUser added to that queue
    # totalPeopleCount = QueueUser.objects.filter(queue_fk=getQueue_fk).count()
    # myQueueObj = Queue.objects.get(id=getQueue_fk) # get single obj
    # # partial= true , is patch update ( thus imp )
    # qSerializer = QueueSerializer(instance=myQueueObj, data= {'totalPeople' : totalPeopleCount}, partial = True)
    
    # if qSerializer.is_valid():
    #     qSerializer.save()
    #     print(qSerializer.data)
    # #! end of queue DB modifictaion


    getEmail = userObj.userAcc_name  # do not move this line up

    #Todo : uncomment this later , when you are in production
    #? this might send email to wrong emails ( since i'm using false emails)
    email = EmailMessage(
        'You are removed from queue :',                   # subject test here 
        'if you think this email was sent to you by mistake, please ignore this message',        # body text here 
        settings.EMAIL_HOST_USER,    # sender's email from settigs.py 
        [getEmail],    # whom to send email (userAcc_name contains email)
        )
    email.fail_silently=False  # will sent us email notifying in case of any error
    email.send()    

    return Response(f"Deleted {id}")


# dont need this here , as uid and id are the same 
@api_view(['DELETE' , 'GET'])
def deleteQueueUserByUid(request,uid):
    userObj = QueueUser.objects.get(g_uid=uid)  #! just changed uid here 
    userObj.delete()
    return Response(f"Deleted by uid {uid}")


@api_view(['POST'])
def notifyUpcomingUserByEmail(request):
    my_userAcc_name = request.data.get('userAcc_name')

    email = EmailMessage(
        'Your number in queue is expected soon :',             # subject test here 
        'if you think this email was sent to you by mistake, please ignore this message',    # body text here 
        settings.EMAIL_HOST_USER,    # sender's email from settigs.py 
        [my_userAcc_name],    # whom to send email (userAcc_name contains email)
        )
    email.fail_silently=False  # will sent us email notifying in case of any error
    email.send()  

    return Response(f"Email sent successfully")

