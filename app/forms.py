from django import forms
from app.models import *

#c=[['Cricket','Cricket'],('Hockey','Hockey'),['Badminton','Badminton']]

class TopicForm(forms.Form):
    topic_name=forms.CharField()


class WebPageForm(forms.Form):
    t1=[[to.topic_name,to.topic_name] for to in Topic.objects.all()]
    topic_name=forms.ChoiceField(choices=t1)
    name=forms.CharField()
    url=forms.URLField()
    email=forms.EmailField()


class AccessRecordForm(forms.Form):
    na=[[na.pk,na.name] for na in WebPage.objects.all()]
    name=forms.ChoiceField(choices=na)
    date=forms.DateField()
    author=forms.CharField()
