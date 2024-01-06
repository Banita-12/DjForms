from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *

# Create your views here.

def djTopic(request):
    ENTO=TopicForm()
    d={'ENTO':ENTO}

    if request.method=='POST':
        NFDO=TopicForm(request.POST)
        if NFDO.is_valid():
            tn=NFDO.cleaned_data['topic_name']   
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()

            QLTO=Topic.objects.all()
            d1={'topic':QLTO}

            #return HttpResponse(str(NFDO.cleaned_data))
            #return HttpResponse(NFDO.cleaned_data['Sname'])
            return render(request,'display_topic.html',d1)


        else:
            return HttpResponse('Data is not Valid')

    return render(request,'djTopic.html',d)

def djWebpage(request):
    ENWO=WebPageForm()
    d={'ENWO':ENWO}

    if request.method=='POST':
        NFWO=WebPageForm(request.POST)
        if NFWO.is_valid():
            tn=NFWO.cleaned_data['topic_name']   
            na=NFWO.cleaned_data['name']
            ur=NFWO.cleaned_data['url']
            em=NFWO.cleaned_data['email']

            TO=Topic.objects.get(topic_name=tn)
            WO=WebPage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
            WO.save()

            QLWO=WebPage.objects.all()
            d1={'webpage':QLWO}
            return render(request,'display_webpage.html',d1)
        else:
            return HttpResponse('Data is not valid')
    return render(request,'djWebpage.html',d)

def djAccessrecord(request):
    ENAO=AccessRecordForm()
    d={'ENAO':ENAO}

    if request.method=='POST':
        NFAO=AccessRecordForm(request.POST)
        if NFAO.is_valid():
            #pk=NFAO.cleaned_data['pk']
            na=NFAO.cleaned_data['name']
            dt=NFAO.cleaned_data['date']
            au=NFAO.cleaned_data['author']

            WO=WebPage.objects.get(pk=na)
            AO=AccessRecord.objects.get_or_create(name=WO,date=dt,author=au)[0]
            AO.save()

            QLAO=AccessRecord.objects.all()
            d1={'accessrecord':QLAO}
            return render(request,'display_accessrecord.html',d1)
        else:
            return HttpResponse('Data is not valid')
        

    return render(request,'djAccessrecord.html',d)