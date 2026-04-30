from django.contrib import admin
from .models import Cha, chaReview,store,chaCertificate

# Register your models here.
class chaReviewInline(admin.TabularInline):    #TabularInline is used to show it's model fields inside the connected or relational model in admin panel.
    model = chaReview                          #We can find the chaReview models field inside cha model.      
    extra = 2


class ChaAdmin(admin.ModelAdmin):
    list_display = ('name','date','chaType')
    inlines = [chaReviewInline]

class storeAdmin(admin.ModelAdmin):
    list_display = ('name','location')
    filter_horizontal = ('cha_varieties',)

class chaCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai','certificate_number')


admin.site.register(Cha, ChaAdmin)
admin.site.register(store, storeAdmin)
admin.site.register(chaCertificate, chaCertificateAdmin)
