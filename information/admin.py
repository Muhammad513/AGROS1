from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register([NarxnomaS])


class BajarilgansihlarAdmin(admin.ModelAdmin):

    @admin.display(description="Bajarilganishlar")
    def admin_date(self,obj):
        return obj.date.strftime('%d-%m-%Y')
    list_display = ('admin_date', 'brigada', 'ish_turi','miqdor','n_summa','k_summa')


admin.site.register(BajarilganIshlar,BajarilgansihlarAdmin)    