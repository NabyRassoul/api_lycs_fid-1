
# Register your models here.
from django.contrib import admin
from .models import*
from api_lycs_fids import*

class UserAdmin(admin.ModelAdmin):
    pass
class PartnerAdmin(admin.ModelAdmin):
    pass
class ClientAdmin(admin.ModelAdmin):
    pass
class VuesAdmin(admin.ModelAdmin):
    pass
class ArticlAdmin(admin.ModelAdmin):
    pass
class BonReductionAdmin(admin.ModelAdmin):
    pass
class CampagneAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Article, ArticlAdmin)
admin.site.register(Campagne, CampagneAdmin)
admin.site.register(BonReduction, BonReductionAdmin)

