from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from home.models import *

admin.site.register(Activity)
admin.site.register(Activity_Species)  
admin.site.register(Continent) 
admin.site.register(Country)
admin.site.register(Family) 
admin.site.register(Genus)
admin.site.register(Geo_Location) 
admin.site.register(Geo_Location_Species)
admin.site.register(IUCN) 
admin.site.register(Micro_Habitat)
admin.site.register(Micro_Habitat_Species) 
admin.site.register(Nesting_Site)
admin.site.register(Nesting_Site_Species) 
admin.site.register(Order_Taxon)
admin.site.register(Parity_Mode) 
admin.site.register(Pop_Trend)
admin.site.register(User_Profile)
admin.site.register(Species)



class UserProfileInline(admin.StackedInline):
    model = User_Profile
    can_delete = False

class AccountsUserAdmin(AuthUserAdmin):
    def add_view(self, *args, **kwargs):
        self.inlines =[UserProfileInline]
        return super(AccountsUserAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines =[UserProfileInline]
        return super(AccountsUserAdmin, self).change_view(*args, **kwargs)


admin.site.unregister(User)
admin.site.register(User, AccountsUserAdmin)




