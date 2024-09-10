from django.shortcuts import render, get_object_or_404
from .models import Body, Member, Achievement, Portal, TechStack, Cabinet, WorkReport, InterIIT, ProblemStatements, Gallery

def home(request):
    workreports = WorkReport.objects.all().order_by('-title').reverse()
    gallery = Gallery.objects.all()
    return render(request, 'home.html', {'workreports': workreports, 'gallery': gallery})

def clubs_list(request):
    clubs = Body.objects.filter(type=0)
    return render(request, 'body_list.html', {'bodies': clubs , 'type': 'Clubs'})

def techteam_list(request):
    techteam = Body.objects.filter(type=1)
    return render(request, 'body_list.html', {'bodies': techteam , 'type': 'Tech Teams'})

def otherbodies_list(request):
    otherbodies = Body.objects.filter(type=2)
    return render(request, 'body_list.html', {'bodies': otherbodies , 'type': 'Other Bodies'})

def body_detail(request, name):
    body = get_object_or_404(Body, name=name)
    members = Member.objects.filter(body=body)
    return render(request, 'body_detail.html', {'body': body, 'members': members})

def portal_list(request):
    portals = Portal.objects.all()
    return render(request, 'portal_list.html', {'portals': portals})

def achievement_list(request):
    achievements = Achievement.objects.all()
    return render(request, 'achievement_list.html', {'achievements': achievements})

def halloffame_list(request):
    halloffame = Achievement.objects.all()
    return render(request, 'halloffame_list.html', {'halloffame': halloffame})

def contact(request):
    cabinet = Cabinet.objects.all()
    return render(request, 'contact.html', {'cabinet': cabinet})
