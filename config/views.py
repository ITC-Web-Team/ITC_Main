from django.shortcuts import render, get_object_or_404
from .models import Body, Member, Achievement, Portal, TechStack, Cabinet, WorkReport, InterIIT, ProblemStatements, Gallery
from collections import defaultdict

def home(request):
    workreports = WorkReport.objects.all().order_by('-title').reverse()
    gallery = Gallery.objects.all()
    return render(request, 'home.html', {'workreports': workreports, 'gallery': gallery})

def clubs_list(request):
    clubs = Body.objects.filter(type=0).order_by('name')
    return render(request, 'body_list.html', {'bodies': clubs , 'type': 'CLUBS'})

def techteam_list(request):
    techteam = Body.objects.filter(type=1).order_by('name')
    return render(request, 'body_list.html', {'bodies': techteam , 'type': 'TECH TEAMS'})

def otherbodies_list(request):
    otherbodies = Body.objects.filter(type=2).order_by('name')
    return render(request, 'body_list.html', {'bodies': otherbodies , 'type': 'COMMUNITIES'})

def body_detail(request, name):
    body = get_object_or_404(Body, name=name)
    members = Member.objects.filter(body=body)
    return render(request, 'body_detail.html', {'body': body, 'members': members})

def portal_list(request):
    portals = Portal.objects.all().order_by('name')
    return render(request, 'portal_list.html', {'portals': portals})

def achievement_list(request):
    bodylist = Body.objects.all()
    selected_body = request.GET.get('body', '')
    
    if selected_body:
        achievements = Achievement.objects.filter(body__name=selected_body)
    else:
        achievements = Achievement.objects.all()
    
    achievements_by_year = defaultdict(list)
    for achievement in achievements.order_by('-date'):
        achievements_by_year[achievement.date.year].append(achievement)
    
    sorted_achievements = dict(sorted(achievements_by_year.items(), reverse=True))
    
    context = {
        'achievements_by_year': sorted_achievements,
        'bodylist': bodylist,
        'selected_body': selected_body,
    }
    return render(request, 'achievements.html', context)

def achievement_detail(request, name):
    body = get_object_or_404(Body, name = name)    
    achievements = Achievement.objects.filter(body=body)

    bodylist = Achievement.objects.all()
    return render(request, 'achievement_list.html', {'achievements': achievements, 'bodylist': bodylist})

def halloffame(request):
    interiit_list = InterIIT.objects.all().order_by('year').reverse()
    problemstatements = ProblemStatements.objects.all()
    return render(request, 'halloffame.html', {'interiit_list': interiit_list, 'problemstatements': problemstatements})

def contact(request):
    cabinet = Cabinet.objects.all()
    return render(request, 'contact.html', {'cabinet': cabinet})
