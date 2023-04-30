from django.contrib import admin

from .models import *


class HeroAdmin(admin.ModelAdmin):
    model = Hero
    filter_horizontal = ("rarity", "classes", "skills",
                         "factions", "bonds_lock")


admin.site.register(Hero, HeroAdmin)
admin.site.register(Rarity)
admin.site.register(Class)
admin.site.register(Skill)
admin.site.register(Faction)
admin.site.register(SkillType)
admin.site.register(SpanType)
