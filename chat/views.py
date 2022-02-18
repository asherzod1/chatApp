import json

from django.shortcuts import render
from .models import *
from django.http.response import JsonResponse, HttpResponse
# Create your views here.

def home(request):
    groups = Group.objects.all()
    return render(
        request=request,
        template_name='index.html',
        context={
            'groups': groups,
        }
    )

def group(request, id):
    groupp = Group.objects.get(id=id)
    return render(
        request=request,
        template_name='group.html',
        context={
            'group': groupp
        }
    )

def comment(request,id):
    if request.method == 'POST':
        if request.user.username:
            data = json.loads(request.body)
            comment = data.get('comment', None)
            group = Group.objects.get(id=id)
            person = Person.objects.get(user=request.user)
            if comment:
                group.setcomment(
                    comment=comment,
                    person=person,
                )
                return HttpResponse(status=201)

