
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clubs', views.clubs_list, name='club_list'),
    path('tectteam/', views.techteam_list, name='techteam_list'),
    path('otherbodies/', views.otherbodies_list, name='otherbodies_list'),
    path('bodies/<str:name>/', views.body_detail, name='body_detail'),
    path('portals/', views.portal_list, name='portal_list'),
    path('achievement/', views.achievement_list, name='achievement_list'),
    path('halloffame/', views.halloffame_list, name='halloffame_list'),
    path('contact/', views.contact, name='contact'),

]
