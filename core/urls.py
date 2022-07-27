from django.urls import path
from . import views

urlpatterns = [

    #! superadmin paths
    path('sa/checkSuperAdmin/', views.checkSuperAdmin),


    #! UserAcc paths
    path('userAcc/', views.getAll_UserAcc),
    path('userAcc/<int:id>/', views.getSingle_UserAcc),
    path('userAcc/register/', views.register_UserAcc),  #add
    path('userAcc/resetAccount/<int:id>/', views.update_UserAcc),  #update , (use for reset password)
    path('userAcc/delete/<int:id>/', views.delete_UserAcc),    #delete

    path('userAcc/login_userAcc/', views.login_UserAcc),
    path('userAcc/forgotPasword_userAcc/', views.forgotPasword_userAcc),
    path('userAcc/verify_userEmail_beforeRegister/', views.verify_UserEmail_beforeRegister),
    

    #! AdminAcc paths
    path('adminAcc/', views.getAll_AdminAcc),
    path('adminAcc/<int:id>/', views.getSingle_AdminAcc),
    path('adminAcc/register/', views.register_AdminAcc),  #add
    path('adminAcc/resetAccount/<int:id>/', views.update_AdminAcc),  #update , (use for reset password)
    path('adminAcc/delete/<int:id>/', views.delete_AdminAcc),    #delete

    path('adminAcc/login_adminAcc/', views.login_AdminAcc),
    path('adminAcc/forgotPasword_adminAcc/', views.forgotPasword_AdminAcc),
    path('adminAcc/verify_adminEmail_beforeRegister/', views.verify_AdminEmail_beforeRegister),
    
   
    #! Queue paths 
    path('queue/', views.getQueue),
    path('queue/<int:id>/', views.getSingleQueue),
    path('queue/add/', views.addQueue),
    path('queue/update/<int:id>/', views.updateQueue),
    path('queue/delete/<int:id>/', views.deleteQueue),
    path('queue/deleteByUid/<int:uid>/', views.deleteQueueByUid), # delete by uid ( dont need now as uid=id)
    
    
    #! Queue User paths 
    path('queueUser/', views.getQueueUser),
    path('queueUser/<int:id>/', views.getSingleQueueUser),
    path('queueUser/add/', views.addQueueUser),
    path('queueUser/update/<int:id>/', views.updateQueueUser),
    path('queueUser/delete/<int:id>/', views.deleteQueueUser),
    path('queueUser/deleteByUid/<int:uid>/', views.deleteQueueUserByUid), # delete by uid ( dont need now as uid=id)


]










