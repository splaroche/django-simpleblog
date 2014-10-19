from django.contrib import admin

from blog.models import Category, Entry


class EntryAdmin(admin.ModelAdmin):
    exclude = ['posted', 'author']
    prepopulated_fields = {'slug': ('title', )}

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
