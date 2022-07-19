from django.contrib import admin
from .models import Departments,Doctors,Booking
# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'pname', 'pnumber','paddress','pemail','doc_name','bdate','bdateon')
    

admin.site.register(Booking, BookingAdmin)