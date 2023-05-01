from django.db import models
from django.urls import reverse


class Hero(models.Model):
    hero_id = models.CharField(max_length=255, primary_key=True)
    hero_name = models.CharField(max_length=255, blank=True)
    hero_icon = models.ImageField(upload_to="hero_icons/", blank=True)
    hero_image = models.ImageField(upload_to="hero_images/", blank=True)
    talent_name = models.CharField(max_length=255, blank=True)
    talent_image = models.ImageField(upload_to="talents/", blank=True)
    talent = models.TextField(blank=True)
    sp_talent_name = models.CharField(max_length=255, blank=True)
    sp_talent_image = models.ImageField(upload_to="sp_talents/", blank=True)
    sp_talent = models.TextField(blank=True)
    class_1_name = models.CharField(max_length=255, blank=True)
    class_1_stats = models.TextField(blank=True)
    class_2_name = models.CharField(max_length=255, blank=True)
    class_2_stats = models.TextField(blank=True)
    class_3_name = models.CharField(max_length=255, blank=True)
    class_3_stats = models.TextField(blank=True)
    exclusive_name = models.CharField(max_length=255, blank=True)
    exclusive_image = models.ImageField(upload_to="exclusive_equipment/",
                                        blank=True)
    exclusive = models.TextField(blank=True)
    casting_pattern_name = models.CharField(max_length=255, blank=True)
    casting_pattern_image = models.ImageField(
        upload_to="casting_patterns/",
        blank=True)
    casting_pattern = models.TextField(blank=True)
    rarity = models.ManyToManyField("Rarity", related_name="heroes",
                                    blank=True)
    classes = models.ManyToManyField("Class", related_name="heroes",
                                     blank=True)
    skills = models.ManyToManyField("Skill", related_name="heroes",
                                    blank=True)
    factions = models.ManyToManyField("Faction", related_name="heroes",
                                      blank=True)
    bonds_lock = models.ManyToManyField(
        "Hero", related_name="bond_unlock", blank=True, symmetrical=False
    )

    def get_absolute_url(self):
        return reverse("hero_page", kwargs={"hero_url": self.hero_id})

    class Meta:
        verbose_name = "Герой"
        verbose_name_plural = "Герои"
        ordering = ["hero_id"]


class Rarity(models.Model):
    rarity_id = models.CharField(max_length=255, primary_key=True)
    rarity_name = models.CharField(max_length=255)
    rarity_image = models.ImageField(upload_to="rarity/", blank=True)


class Class(models.Model):
    class_id = models.CharField(max_length=255, primary_key=True)
    class_name = models.CharField(max_length=255)
    class_image = models.ImageField(upload_to="classes/", blank=True)


class Skill(models.Model):
    skill_id = models.CharField(max_length=255, primary_key=True)
    skill_name = models.CharField(max_length=255, blank=True)
    skill_image = models.ImageField(upload_to="skills/", blank=True)
    skill_cost = models.IntegerField(blank=True)
    skill_cd = models.IntegerField(blank=True)
    skill_range = models.IntegerField(blank=True)
    skill_span = models.IntegerField(blank=True)
    skill = models.TextField(blank=True)
    type = models.ManyToManyField("SkillType", related_name="skills",
                                  blank=True)
    span_type = models.ManyToManyField("SpanType", related_name="skills",
                                       blank=True)


class Faction(models.Model):
    faction_id = models.CharField(max_length=255, primary_key=True)
    faction_name = models.CharField(max_length=255)
    faction_image = models.ImageField(upload_to="factions/", blank=True)


class SkillType(models.Model):
    skill_type_id = models.CharField(max_length=255, primary_key=True)
    skill_type_name = models.CharField(max_length=255)
    skill_type_image = models.ImageField(upload_to="skill_types/", blank=True)


class SpanType(models.Model):
    span_id = models.CharField(max_length=255, primary_key=True)
    span_name = models.CharField(max_length=255)
    span_image = models.ImageField(upload_to="span_types/", blank=True)
