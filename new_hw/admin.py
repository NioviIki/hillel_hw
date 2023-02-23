from django.contrib import admin
from .models import Author, Publisher, Book, Store


admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Store)

# @admin.register(Author, Publisher, Book, Store)
# class ModelAdmin(admin.ModelAdmin):
    # list_display = ('method_of_request', 'path_of_request', 'date_and_time')
    #
    # list_filter = ['date_and_time']
    # fieldsets = [("Method and Path",
    #               {'fields': ('method_of_request', 'path_of_request'),
    #                'classes': ('wide', )}
    #               ),
    #              ('JSON', {'fields': ('query_data', 'body_data'), 'classes': ('wide', )})
    #              ]
    # search_fields = ['method_of_request', 'path_of_request', 'date_and_time']
    #
    # date_hierarchy = 'date_and_time'
    # list_per_page = 20

