from django.contrib import admin
from registration_app.models import useraccount
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin

admin.site.site_header = 'Demo Dashboard'

class useraccountAdmin(ImportExportModelAdmin):
    # list_display = ('username', 'email')
    # list_filter = ('username')
    # search_fields = ('username', 'email')
    # ordering = ('id', )
    pass



admin.site.register(useraccount, useraccountAdmin)


admin.site.unregister(Group)



