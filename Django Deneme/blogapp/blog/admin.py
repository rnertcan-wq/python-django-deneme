from django.contrib import admin
from.models import Blog, Category


# Register your models here.
class Blogadmin(admin.ModelAdmin):
    list_display = ("title", "is_activate", "is_home", "slug",)
    list_editable = ("is_activate", "is_home",)
    search_fields = ("title", "description",)
    readonly_fields = ("slug",)
    list_filter = ("category", "is_activate", "is_home")


admin.site.register(Blog, Blogadmin)
admin.site.register(Category,)