from django.contrib import admin
from django.urls import path, include
from .views import home, clubs_list, techteam_list, otherbodies_list, body_detail, portal_list, achievement_list, achievement_detail, halloffame, contact
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
from django.http import HttpResponse

sitemaps = {
    'static': StaticViewSitemap,
}

def robots_txt(request):
    content = "User-agent: *\nDisallow: /admin/\nSitemap: https://yourdomain.com/sitemap.xml"
    return HttpResponse(content, content_type="text/plain")



urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('robots.txt', robots_txt),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('clubs', clubs_list, name='club_list'),
    path('tectteam/', techteam_list, name='techteam_list'),
    path('otherbodies/', otherbodies_list, name='otherbodies_list'),
    path('bodies/<str:name>/', body_detail, name='body_detail'),
    path('portals/', portal_list, name='portal_list'),
    path('achievements/', achievement_list, name='achievement_list'),
    path('achievement/<str:name>/', achievement_detail, name='achievement_detail'),
    path('halloffame/', halloffame, name='halloffame_list'),
    path('contact/', contact, name='contact'),
    path('', home, name='home'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


