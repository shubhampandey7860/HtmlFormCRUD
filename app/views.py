from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def topic(request):
    if request.method == 'POST':
        topic_name = request.POST['topic_name']
        T = Topic.objects.get_or_create(topic_name = topic_name)[0]
        T.save()
        return HttpResponse('topic_name submited succesfully')
    return render(request,'topic.html')

# webpage
def webpage(request):
    QST = Topic.objects.all()
    d={'QST':QST}
    if request.method=='POST':
        topic_name = request.POST['topic']
        name = request.POST['name']
        url = request.POST['url']
        T = Topic.objects.get_or_create(topic_name=topic_name)[0]
        T.save()
        w=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
        w.save()
        return HttpResponse('webpage data is inserted succesfully')
    return render(request,'webpage.html',d)

# AccessRecord
# def Access(request):
#     T=Topic.objects.all()
#     d={'QST':T}
#     if request.method=='POST':
#         topic_name = request.POST['topic_name']
#         name = request.POST['name']
#         url = request.POST['url']
#         date = request.POST['date']
#         T = Topic.objects.get_or_create(topic_name=topic_name)[0]
#         T.save()
#         w=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
#         w.save()
#         A = AccessRecord.objects.get_or_create(name=w,date=date)
#         return HttpResponse('Access data is inserted succesfully')
#     return render(request,'Access.html',d)
    
def show_topic(request):
    T = Topic.objects.all()
    d={'QST':T}
    return render(request,'show_topic.html',d)
def show_webpage(request):
    w =  Webpage.objects.all()
    d={'QSW':w}
    return render(request,'show_webpage.html',d)

def show_Access(request):
    A = AccessRecord.objects.all()
    d={'QSA':A}
    return render(request,'show_Access.html',d)

def delete_Topic(request):
    t= Topic.objects.all().delete()
    return render(request,'show_topic.html')

def show_specific_record(request):
    T=Topic.objects.all()
    QST={'QST':T}
    if request.method=="POST":
        topic=request.POST['topic']
        if topic=='Cricket':
            w=Webpage.objects.filter(topic_name=topic)
            d={'QSW':w}
            return render(request,'show_webpage.html',d)
        elif topic=='FootBall':
            w=Webpage.objects.filter(topic_name=topic)
            d={'QSW':w}
            return render(request,'show_webpage.html',d)
        elif topic=='Kabaddi':
            w=Webpage.objects.filter(topic_name=topic)
            d={'QSW':w}
            return render(request,'show_webpage.html',d)
        elif topic=='Hockey':
            w=Webpage.objects.filter(topic_name=topic)
            d={'QSW':w}
            return render(request,'show_webpage.html',d)
    return render(request,'search.html',QST)  

def select_multiple(request):
    T=Topic.objects.all()
    QST={'QST':T}
    if request.method=="POST":
        topic=request.POST.getlist('topic')
        w=Webpage.objects.none()
        for i in topic:
            w=w|Webpage.objects.filter(topic_name=i)
        d1={'QSW':w}
        return render(request,'show_webpage.html',d1)
            
    
    return render(request,'select_multiple.html',QST) 
def checkBox(request):
    T=Topic.objects.all()
    QST={'QST':T}
    return render(request,'checkBox.html',QST) 

    
 
            
    
   
            
           
            
    
        
    

    
           