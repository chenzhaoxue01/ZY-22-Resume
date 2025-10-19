from django.contrib import admin
from .models import PersonalInfo, Education, Skill, Project, Experience

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'student_id', 'major', 'email', 'phone']
    search_fields = ['name', 'student_id', 'major']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['personal_info', 'school', 'degree', 'major', 'start_date', 'end_date']
    list_filter = ['degree', 'school']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['personal_info', 'name', 'level']
    list_filter = ['level']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['personal_info', 'name', 'role', 'start_date', 'end_date']
    search_fields = ['name', 'technologies']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['personal_info', 'company', 'position', 'start_date', 'end_date']
    search_fields = ['company', 'position']