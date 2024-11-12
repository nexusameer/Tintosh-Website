from django.contrib import admin
from .models import *

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('happy_clients', 'project_completed', 'years_of_experience', 'email')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'project_category', 'url')
    search_fields = ('name', 'project_category')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'facebook_profile', 'linkedin_profile', 'github_profile', 'twitter_profile')
    search_fields = ('name', 'role')

@admin.register(FeaturedClient)
class FeaturedClientAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    search_fields = ('name', )

@admin.register(Testimonals)
class TestimonalsAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'designation')