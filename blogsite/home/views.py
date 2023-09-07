from django.shortcuts import render,get_object_or_404
from . models import *



# Create your views here.
def loadindex(request):
     #For Displaying
    obj=blogpost.objects.all()   
    obj1=latestpost.objects.all()
                 
    return render(request,'index.html',{'data':obj ,'data1':obj1})

def loadsinglepost(request,id):  
    obj1=get_object_or_404(blogpost,pk=id)  #pk keyword,blogpost=Table
    return render(request,'single-post.html',{'d1':obj1})

def loadaboutus(request):    
    return render(request,'about-us.html')

def loadcontactus(request):    
    return render(request,'contactus.html')




