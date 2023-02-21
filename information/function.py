from .models import*
from django.db.models import Sum,Count,Q
from django.db.models import  F,IntegerField,FloatField
import datetime




def hudud_list(obj,hud_num):
    hudud=[]
    lists=obj.objects.filter(hudud__h_num=hud_num).values("br_num")
    for i in lists:
        num=i["br_num"]
        hudud.append(num)
    return hudud    
    


def datenow(date):
    if date is None:
        x=datetime.datetime.now()
        date=x.strftime("%Y-%m-%d")
    else:
        date=date
    return date    



#--------------------ARIQ------------------------------------------------------------------------------------------
def baj_ish(obj,hudud,code,code2): 
    baj=obj.objects.filter(hudud__h_num=hudud).annotate(
            miqdor=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=code)),
            n_summa=Sum('bajarilganishlar__n_summa',filter=Q(bajarilganishlar__ish_turi__code=code)),
            k_summa=Sum('bajarilganishlar__k_summa',filter=Q(bajarilganishlar__ish_turi__code=code)),
            miqdor1=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=code2)),
            n_summa1=Sum('bajarilganishlar__n_summa',filter=Q(bajarilganishlar__ish_turi__code=code2)),
            k_summa1=Sum('bajarilganishlar__k_summa',filter=Q(bajarilganishlar__ish_turi__code=code2)),
        )
    baj=baj.values('br_num',"massiv__name",'br_full_name',"P_gektar",'miqdor','n_summa',"k_summa",'miqdor1','n_summa1',"k_summa1")
    return baj

#-----------------ARIQ BIRKUNDA----------------------------------------------------------------------------------------------------
def baj_ish_data(obj,hudud,date,br_list,code,code1): 
    lists=[]
    for i in br_list:
        result=obj.objects.filter(hudud__h_num=hudud,br_num=i,bajarilganishlar__date=date).aggregate(
        birkunda=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=code)),
        birkunda1=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=code1))
            )
        result1=result["birkunda"]
        result2=result["birkunda1"]
        
        lists.append({ f"birkunda":result1,"birkunda1":result2})    
        
    return lists
#--------------PAXTA SUV----------------------------------------------------------------------------------------------------------------------
def baj_suv(obj,hudud,suv1,suv2,suv3,suv4,suv5,suv6): 
    baj=obj.objects.filter(hudud__h_num=hudud).annotate(
            miqdor1=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv1),output_field=FloatField()),
            qoldiq1=(F('P_gektar')-Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv1),default=0,output_field=FloatField())),
            
            miqdor2=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv2)),
            qoldiq2=(F('P_gektar')-Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv2),default=0,output_field=FloatField())),

            miqdor3=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv3)),
            qoldiq3=(F('P_gektar')-Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv3),default=0,output_field=FloatField())),
            
            miqdor4=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv4)),
            qoldiq4=(F('P_gektar')-Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv4),default=0,output_field=FloatField())),
            
            miqdor5=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv5)),
            qoldiq5=(F('P_gektar')-Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv5),default=0,output_field=FloatField())),
            
            miqdor6=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv6)),
            qoldiq6=(F('P_gektar')-Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv6),default=0,output_field=FloatField())),
            
               )
    baj=baj.values('br_num',"massiv__name",'br_full_name',"P_gektar",'miqdor1','miqdor2','miqdor3','miqdor4','miqdor5','miqdor6','qoldiq1','qoldiq2','qoldiq3','qoldiq4','qoldiq5','qoldiq6')
    return baj
#----------------------PAXTA SUV BIRKUNDA-------------------------------------------------------------------------------
def baj_suv_data(obj,hudud,date,br_list,code1,code2,code3,code4,code5,code6): 
    lists=[]
    for i in br_list:
        result=obj.objects.filter(hudud__h_num=hudud,br_num=i,bajarilganishlar__date=date).aggregate(
        birkunda1=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=code1)),
        birkunda2=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=code2)),
        birkunda3=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=code3)),
        birkunda4=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=code4)),
        birkunda5=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=code5)),
        birkunda6=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=code6)),
            )
                   
        result1=result["birkunda1"]
        result2=result["birkunda2"]
        result3=result["birkunda3"]
        result4=result["birkunda4"]
        result5=result["birkunda5"]
        result6=result["birkunda6"]
        if result1:
            result1
        else:
            result1=0    
        if result2:
            result2
        else:
            result2=0    
        
        if result3:
            result3
        else:
            result3=0    
        
        if result4:
            result4
        else:
            result4=0
        if result5:
            result5
        else:
            result5=0
        if result6:
            result6
        else:
            result6=0            
        result5=result1+result2+result3+result4+result5+result6
        lists.append({"birkunda":result5})    
    return lists


def baj_suv_g(obj,hudud,suv1,suv2,suv3,suv4,suv5,suv6): 
    baj=obj.objects.filter(hudud__h_num=hudud).annotate(
            miqdor1=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv1), output_field=FloatField()),
            n_summa1=Sum('bajarilganishlar__n_summa',filter=Q(bajarilganishlar__ish_turi__code=suv1), output_field=FloatField()),
            k_summa1=Sum('bajarilganishlar__k_summa',filter=Q(bajarilganishlar__ish_turi__code=suv1), output_field=FloatField()),
            qoldiq1=(F('G_gektar')-Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv1),default=0,output_field=FloatField())),

            miqdor2=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv2), output_field=FloatField()),
            n_summa2=Sum('bajarilganishlar__n_summa',filter=Q(bajarilganishlar__ish_turi__code=suv2), output_field=FloatField()),
            k_summa2=Sum('bajarilganishlar__k_summa',filter=Q(bajarilganishlar__ish_turi__code=suv2), output_field=FloatField()),
            qoldiq2=(F('G_gektar')-Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv2),default=0,output_field=FloatField())),


            miqdor3=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv3), output_field=FloatField()),
            n_summa3=Sum('bajarilganishlar__n_summa',filter=Q(bajarilganishlar__ish_turi__code=suv3), output_field=FloatField()),
            k_summa3=Sum('bajarilganishlar__k_summa',filter=Q(bajarilganishlar__ish_turi__code=suv3), output_field=FloatField()),
            qoldiq3=(F('G_gektar')-Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv3),default=0,output_field=FloatField())),
            
            miqdor4=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv4), output_field=FloatField()),
            n_summa4=Sum('bajarilganishlar__n_summa',filter=Q(bajarilganishlar__ish_turi__code=suv4), output_field=FloatField()),
            k_summa4=Sum('bajarilganishlar__k_summa',filter=Q(bajarilganishlar__ish_turi__code=suv4), output_field=FloatField()),
            qoldiq4=(F('G_gektar')-Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv4),default=0,output_field=FloatField())),

            miqdor5=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv5), output_field=FloatField()),
            n_summa5=Sum('bajarilganishlar__n_summa',filter=Q(bajarilganishlar__ish_turi__code=suv5), output_field=FloatField()),
            k_summa5=Sum('bajarilganishlar__k_summa',filter=Q(bajarilganishlar__ish_turi__code=suv5), output_field=FloatField()),
            qoldiq5=(F('G_gektar')-Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv5),default=0,output_field=FloatField())),

            miqdor6=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv6), output_field=FloatField()),
            n_summa6=Sum('bajarilganishlar__n_summa',filter=Q(bajarilganishlar__ish_turi__code=suv6), output_field=FloatField()),
            k_summa6=Sum('bajarilganishlar__k_summa',filter=Q(bajarilganishlar__ish_turi__code=suv6), output_field=FloatField()),
            qoldiq6=(F('G_gektar')-Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=suv6),default=0,output_field=FloatField())),


               )
    baj=baj.values(
        'br_num',"massiv__name",'br_full_name',"G_gektar",
        'miqdor1','n_summa1',"k_summa1",'miqdor2','n_summa2',"k_summa2",
        'miqdor3','n_summa3',"k_summa3",'miqdor4','n_summa4',"k_summa4",
        'miqdor4','n_summa4',"k_summa4",'miqdor5','n_summa5',"k_summa5",
        'miqdor6','n_summa6',"k_summa6",'qoldiq1','qoldiq2','qoldiq3','qoldiq4','qoldiq5','qoldiq6',
    )
    return baj





def baj_suv_data_g(obj,hudud,date,br_list,code1,code2,code3,code4,code5,code6): 
    lists=[]
    for i in br_list:
        result=obj.objects.filter(hudud__h_num=hudud,br_num=i,bajarilganishlar__date=date).aggregate(
        birkunda1=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=code1),default=0),
        birkunda2=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=code2),default=0),
        birkunda3=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=code3),default=0),
        birkunda4=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=code4),default=0),
        birkunda5=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=code5),default=0),
        birkunda6=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=code6),default=0),
            )
                   
        result1=result["birkunda1"]
        result2=result["birkunda2"]
        result3=result["birkunda3"]
        result4=result["birkunda4"]
        result5=result["birkunda5"]
        result6=result["birkunda6"]
                
        result7=result1+result2+result3+result4+result5+result6
        lists.append({"birkunda":result7})    
    return lists


def baj_ish_1(obj,hudud,code): 
    baj=obj.objects.filter(hudud__h_num=hudud).annotate(
            miqdor=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=code),default=0),
            qoldiq=(F('P_gektar')-Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=code),default=0,output_field=FloatField())),
            
            
        )
    baj=baj.values('br_num',"massiv__name",'br_full_name',"P_gektar",'miqdor',"qoldiq")
    return baj

def baj_b_1(obj,hudud,date,br_list,code1): 
    lists=[]
    for i in br_list:
        result=obj.objects.filter(hudud__h_num=hudud,br_num=i,bajarilganishlar__date=date).aggregate(
        birkunda=Sum('bajarilganishlar__miqdor',filter=Q(bajarilganishlar__ish_turi__code=code1),default=0),
        )
                   
        result1=result["birkunda"]
        lists.append({"birkunda":result1})    
    return lists