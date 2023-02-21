from .models import*
from django.db.models import Sum,Count,Q
from django.db.models import  F,IntegerField,FloatField
import datetime

def datenow(date):
    if date is None:
        x=datetime.datetime.now()
        date=x.strftime("%Y-%m-%d")
    else:
        date=date
    return date    









def item_hudud(obj,num_hudud):
    result=obj.objects.filter(hudud__h_num=num_hudud).annotate(
                        kond_br_sums=Sum(F('paxta__kond')/1000, output_field=FloatField()),
                        sums_skidka=Sum('paxta__kond')/1000-Sum('paxta__sofVazn')/1000,
                        sent=Sum(F('paxta__kond')/F("P_gektar")/100, output_field=FloatField()),
                        bajarilish=Sum(F('paxta__kond')/10/F("P_reja"), output_field=FloatField())
                        )
    
    result=result.values("kond_br_sums","br_num","massiv__name","br_full_name","P_gektar","P_reja","sums_skidka","sent","bajarilish")                    
    return result





def data_br(obj,num_hudud,data,br_list):
    lists=[]
    for i in br_list:
        result=obj.objects.filter(hudud__h_num=num_hudud,paxta__date=data,br_num=i).aggregate(birkunda=Sum('paxta__kond')/1000)
        result=result["birkunda"]
        lists.append({ f"birkunda":result})
    return lists    
#------------------------------------------------------------------------------------

def item_hudud_G(obj,num_hudud):
    result=obj.objects.filter(hudud__h_num=num_hudud).annotate(
                        kond_br_sums=Sum(F('galla__sofVazn')/1000, output_field=FloatField()),
                        sent=Sum(F('galla__sofVazn')/F("G_gektar")/100, output_field=FloatField()),
                        bajarilish=Sum(F('galla__sofVazn')/10/F("G_reja"), output_field=FloatField())
                    )
    
    result=result.values("kond_br_sums","br_num","massiv__name","br_full_name","G_gektar","G_reja","sent","bajarilish")                    
    return result


def data_br_G(obj,num_hudud,data,br_list):
    lists=[]
    for i in br_list:
        result=obj.objects.filter(hudud__h_num=num_hudud,galla__date=data,br_num=i).aggregate(birkunda=Sum('galla__sofVazn')/1000)
        result=result["birkunda"]
        lists.append({ f"birkunda":result})
        
    return lists
def item_ombor_G(obj,ombor):
    result=obj.objects.filter(name=ombor).annotate(
                        sums=Sum(F('galla__sofVazn')/1000, output_field=FloatField()),
                        )
    
    result=result.values("sums",'reja',"sentner","name")                    
    return result


def hudud(obj,hudud):
    result=obj.objects.filter(h_num=hudud).annotate(
                        kond_hudud_sums=Sum(F('brigada__paxta__kond')/1000, output_field=FloatField()),
                        gektar_hudud=Sum(('brigada__P_gektar'), output_field=FloatField()),
                        reja_hudud=Sum(('brigada__P_reja'), output_field=FloatField()),
                        sums_skidka=Sum('brigada__paxta__kond')/1000-Sum('brigada__paxta__sofVazn')/1000,
                        sent=Sum('brigada__paxta__kond')/1000/Sum("brigada__P_gektar")*10,
                        bajarilish=Sum('brigada__paxta__kond')/Sum('brigada__P_reja')/10,
                        )
                        
    
    result=result.values("kond_hudud_sums","h_num",'gektar_hudud',"Agranom_full_name","sums_skidka","sent","bajarilish","reja_hudud")                      
    return result
def hudud_b(obj,num_hudud,data):

    result=obj.objects.filter(h_num=num_hudud,brigada__paxta__date=data).aggregate(birkunda=Sum('brigada__paxta__kond')/1000)
    return [result]


def hudud_g(obj,hudud):
    result=obj.objects.filter(h_num=hudud).annotate(
                        hudud_sums=Sum(F('brigada__galla__sofVazn')/1000, output_field=FloatField()),
                        gektar_hudud=Sum(('brigada__G_gektar'), output_field=FloatField()),
                        reja_hudud=Sum(('brigada__G_reja'), output_field=FloatField()),
                        sums_skidka=Sum('brigada__galla__sofVazn')/1000-Sum('brigada__galla__sofVazn')/1000,
                        sent=Sum('brigada__galla__sofVazn')/1000/Sum("brigada__G_gektar")*10,
                        bajarilish=Sum('brigada__galla__sofVazn')/Sum('brigada__G_reja')/10,
                        )
                        
    
    result=result.values("hudud_sums","h_num",'gektar_hudud',"Agranom_full_name","sums_skidka","sent","bajarilish","reja_hudud")                      
    return result

def hudud_g_b(obj,num_hudud,data):

    result=obj.objects.filter(h_num=num_hudud,brigada__galla__date=data).aggregate(birkunda=Sum('brigada__galla__sofVazn')/1000)
    return [result]
    

def dori(obj,date,code1,code2,code3):
    result=obj.objects.filter().annotate(
        miqdor1=Sum('dorisend__kolvo',filter=Q(dorisend__dori_tur__code=code1),default=0),
        qoldiq1=(F('amaf_reja')-Sum('dorisend__kolvo',filter=Q(dorisend__dori_tur__code=code1),default=0)),
        date1=Sum('dorisend__kolvo',filter=Q(dorisend__dori_tur__code=code1)&Q(dorisend__date=date),default=0),
        
        miqdor2=Sum('dorisend__kolvo',filter=Q(dorisend__dori_tur__code=code2),default=0),
        qoldiq2=(F('karb_reja')-Sum('dorisend__kolvo',filter=Q(dorisend__dori_tur__code=code2),default=0)),
        date2=Sum('dorisend__kolvo',filter=Q(dorisend__dori_tur__code=code2)&Q(dorisend__date=date),default=0),
        
        miqdor3=Sum('dorisend__kolvo',filter=Q(dorisend__dori_tur__code=code3),default=0),
        qoldiq3=(F('kali_reja')-Sum('dorisend__kolvo',filter=Q(dorisend__dori_tur__code=code3),default=0)),
        date3=Sum('dorisend__kolvo',filter=Q(dorisend__dori_tur__code=code3)&Q(dorisend__date=date),default=0),

    )
    result=result.values("id",'fx_name',"maydon","amaf_reja","karb_reja","kali_reja","miqdor1","miqdor2","miqdor3","qoldiq1","qoldiq2","qoldiq3","massiv","date1","date2","date3",)
                  
    return result    






