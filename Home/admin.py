from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(Paxta)
admin.site.register(Punkt)
admin.site.register(Hudud)
admin.site.register([Profile,Friend,ChatMessage,Lavozim,Massiv,Galla,OmborG,Narxnoma,Maxsulot,Ishxaqqi,Xodimlar,Kontragen,DoriOmbor])


class BrigadaAdmin(admin.ModelAdmin):
    list_display = ('br_num', 'br_full_name','massiv', 'G_gektar','P_gektar')

class DoriSendAdmin(admin.ModelAdmin):
    list_display = ('fermer', 'dori_tur','kolvo', 'summa',)




admin.site.register(Brigada,BrigadaAdmin)
admin.site.register(DoriSend,DoriSendAdmin)    