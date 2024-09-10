from django.contrib import admin
from .models import Body, Member, Achievement, Portal, TechStack, Cabinet, WorkReport, InterIIT, ProblemStatements, Gallery

admin.site.register(Body)
admin.site.register(Member)
admin.site.register(Achievement)
admin.site.register(Portal)
admin.site.register(TechStack)
admin.site.register(Cabinet)

admin.site.register(WorkReport)
admin.site.register(Gallery)  

admin.site.register(InterIIT)
admin.site.register(ProblemStatements)