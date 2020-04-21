from django.contrib import admin
from registration_app.models import newUser
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin

admin.site.site_header = 'Demo Dashboard'

class newUserAdmin(ImportExportModelAdmin):
    list_display = ('fullname', 'usrname', 'email')
    list_filter = ('fullname', 'usrname')
    search_fields = ('fullname', 'usrname', 'email')
    ordering = ('id', )
   



admin.site.register(newUser, newUserAdmin)


admin.site.unregister(Group)



