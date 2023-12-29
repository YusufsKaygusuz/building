from django.contrib import admin
from .models import ContactInfo, HeaderIntroduction, AboutUs, Services, Projects, Comments, SocialAccount, Chart, contact_info

# Register your models here.
@admin.register(ContactInfo)
class contactAdmin(admin.ModelAdmin):
    list_display = ("first_telephone", "e_mail_address",)
    prepopulated_fields = {"slug": ("e_mail_address",),}
    


@admin.register(HeaderIntroduction)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ("heading", "slug", "isActive",)
    readonly_fields = ("slug",)
    list_filter = ("isActive",)
    list_editable = ("isActive",)

@admin.register(AboutUs)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("heading", "slug", "isActive",)
    list_filter = ("isActive",)
    list_editable = ("isActive",)
    readonly_fields = ("slug",)

@admin.register(Chart)
class ChartAdmin(admin.ModelAdmin):
    list_display = ("firstChartNumber", "firstChartDescription", "secondChartNumber", "secondChartdescription",)

class contactAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",)
    prepopulated_fields = {"slug": ("e_mail_address",),}


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("heading", "slug", "isActive",)
    list_filter = ("isActive",)
    list_editable = ("isActive",)
    readonly_fields = ("slug",)


@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("heading", "mini_description", "isActive", "isMain")
    list_filter = ("isActive",)
    list_editable = ("isActive", "isMain",)
    readonly_fields = ("slug",)

@admin.register(Comments)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name_surname", "score", "isActive",)
    list_filter = ("isActive",)
    list_editable = ("isActive",)
    readonly_fields = ("slug",)

@admin.register(SocialAccount)
class SocialAdmin(admin.ModelAdmin):
    list_display = ("instaccount",)

@admin.register(contact_info)
class contactAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "e_mail_address",)
    readonly_fields = ("slug",)
