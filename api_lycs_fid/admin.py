from django.contrib import admin
from .models import*
from api_lycs_fid import*

class UserAdmin(admin.ModelAdmin):
    pass
class PartnerAdmin(admin.ModelAdmin):
    pass
class ClientAdmin(admin.ModelAdmin):
    pass
class BonAdmin(admin.ModelAdmin):
    pass
class ArticlAdmin(admin.ModelAdmin):
    pass
class CampagneAdmin(admin.ModelAdmin):
    pass
class LoyaltyAdmin(admin.ModelAdmin):
    pass
class LoyaltyTierAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(LoyaltyProgram, LoyaltyAdmin)
admin.site.register(LoyaltyTier, LoyaltyTierAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Article, ArticlAdmin)
admin.site.register(BonReduction, BonAdmin)
admin.site.register(Campagne, CampagneAdmin)

