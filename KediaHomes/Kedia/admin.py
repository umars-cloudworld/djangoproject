from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from Kedia.models import *
from .forms import *

class OurProjectsAdminView(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'is_active', 'created_at']
    form = OurProjectsForm


class ContactUsAdminView(admin.ModelAdmin):
    list_display = ['id', 'user', 'message' , 'subject', 'name', 'email', 'created_at']


class NewsLetterAdminView(admin.ModelAdmin):
    list_display = ['id', 'user', 'email', 'created_at']


class ProjectsAdminView(admin.ModelAdmin):
    list_display = ['id', 'type', 'name', 'slug','is_active', 'created_at']
    form = ProjectsForm


class PricingAdminView(admin.ModelAdmin):
    def project_name(self, obj):
        return obj.project.name

    list_display = ['id', 'project_name', 'description', 'title', 'icon_class', 'is_active', 'created_at']
    search_fields = ["title"]
    form = PricingForm


class MapInline(admin.TabularInline):
    model = Map
    show_change_link = True


class MapAdminView(admin.ModelAdmin):
    list_display = ['id', 'plot_no', 'Coordinate', 'plot_size', 'direction', 'dimension', 'plc', 'plan', 'floor', 'elevation', 'price', 'created_at']
    search_fields = ['plot_no',]
    # inlines = [MapInline, ]

class Booking_new_admin(ModelAdmin):
    list_display = ['email', 'phone', 'plot_no', 'pan']

class Blog_admin(ModelAdmin):
    list_display=['title', 'img_src','description']

admin.site.register(OurProjects, OurProjectsAdminView)
admin.site.register(ContactUs, ContactUsAdminView)
admin.site.register(NewsLetter, NewsLetterAdminView)
admin.site.register(Projects, ProjectsAdminView)
admin.site.register(Pricing, PricingAdminView)
admin.site.register(Map, MapAdminView)
admin.site.register(Booking_new, Booking_new_admin)
admin.site.register(Blog, Blog_admin)

