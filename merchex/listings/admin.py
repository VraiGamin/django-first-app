from django.contrib import admin
from listings.models import Band, Listing
# Register your models here.


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'year_formed')


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'year', 'sold')


admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
