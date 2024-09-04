from django.shortcuts import render, get_object_or_404
from .models import Body, Member, Achievement, Portal, TechStack, Cabinet, WorkReport

def home(request):
    workreports = WorkReport.objects.all()
    return render(request, 'base/home.html', {'workreports': workreports})

def clubs_list(request):
    clubs = Body.objects.filter(type=0)
    return render(request, 'base/clubs_list.html', {'clubs': clubs})

def techteam_list(request):
    techteam = Body.objects.filter(type=1)
    return render(request, 'base/techteam_list.html', {'techteam': techteam})

def otherbodies_list(request):
    otherbodies = Body.objects.filter(type=2)
    return render(request, 'base/otherbodies_list.html', {'otherbodies': otherbodies})

def body_detail(request, name):
    body = get_object_or_404(Body, name=name)
    members = Member.objects.filter(body=body)
    return render(request, 'base/body_detail.html', {'body': body, 'members': members})

def portal_list(request):
    portals = Portal.objects.all()
    return render(request, 'base/portal_list.html', {'portals': portals})

def achievement_list(request):
    achievements = Achievement.objects.all()
    return render(request, 'base/achievement_list.html', {'achievements': achievements})

def halloffame_list(request):
    halloffame = Achievement.objects.all()
    return render(request, 'base/halloffame_list.html', {'halloffame': halloffame})

def contact(request):
    cabinet = Cabinet.objects.all()
    return render(request, 'base/contact.html', {'cabinet': cabinet})
