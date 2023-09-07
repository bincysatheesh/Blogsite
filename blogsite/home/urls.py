
from django.urls import path,include
from .import views
urlpatterns = [  
    path('',views.loadindex,name='loadindex'),
    path('<int:id>',views.loadsinglepost,name='loadsinglepost'), 
    path('loadaboutus',views.loadaboutus,name='loadaboutus'),
    path('loadcontactus',views.loadcontactus,name='loadcontactus'), 
 
   
]
