from django.contrib import admin
from django.urls import path
from .views import home, clubs_list, techteam_list, otherbodies_list, body_detail, portal_list, achievement_list, achievement_detail, halloffame_list, contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clubs', clubs_list, name='club_list'),
    path('tectteam/', techteam_list, name='techteam_list'),
    path('otherbodies/', otherbodies_list, name='otherbodies_list'),
    path('bodies/<str:name>/', body_detail, name='body_detail'),
    path('portals/', portal_list, name='portal_list'),
    path('achievement/', achievement_list, name='achievement_list'),
    path('achievement/<str:name>/', achievement_detail, name='achievement_detail'),
    path('halloffame/', halloffame_list, name='halloffame_list'),
    path('contact/', contact, name='contact'),
    path('', home, name='home'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
