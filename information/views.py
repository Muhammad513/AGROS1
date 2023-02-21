from django.shortcuts import render
from .models import*
from Home.models import Brigada
from django.db.models import Sum,Count,Q
from django.db.models import  F,IntegerField,FloatField
from .function import*
from Config.settings import agranom1,agranom2,agranom3

# ARIQ CHOPISH
def infors(request):
    date=request.GET.get("date")
    user=request.user.profile
    date=datenow(date)
    #1
    hudud_1=hudud_list(Brigada,1)
    h_1_R15=baj_ish(Brigada,1,"A1","A2")
    birkunda=baj_ish_data(Brigada,1,date,hudud_1,"A1","A2")
    h_1_R15=zip(h_1_R15,birkunda)
    #2
    hudud_2=hudud_list(Brigada,2)
    h_2_R15=baj_ish(Brigada,2,"A1","A2")
    birkunda=baj_ish_data(Brigada,2,date,hudud_2,"A1","A2")
    h_2_R15=zip(h_2_R15,birkunda)
    
    #3
    hudud_3=hudud_list(Brigada,3)
    h_3_R15=baj_ish(Brigada,3,"A1","A2")
    birkunda=baj_ish_data(Brigada,3,date,hudud_3,"A1","A2")
    h_3_R15=zip(h_3_R15,birkunda)
           
    context={"user":user,"h_1_R15":h_1_R15,"h_2_R15":h_2_R15,"h_3_R15":h_3_R15,"date":date,"agranom1":agranom1,"agranom2":agranom2,"agranom3":agranom3}
    return render(request,'ihome.html',context)

# PAXTA SUVI
def p_suv(request):
    date=request.GET.get("date")
    user=request.user.profile
    date=datenow(date)
    #1
    hudud_1=hudud_list(Brigada,1)
    h_1_R15=baj_suv(Brigada,1,"R1","R2","R3","R4","R5","R6")
    birkunda=baj_suv_data(Brigada,1,date,hudud_1,"R1","R2","R3","R4","R5","R6")
    h_1_R15=zip(h_1_R15,birkunda)
   
    #2
    hudud_2=hudud_list(Brigada,2)
    h_2_R15=baj_suv(Brigada,2,"R1","R2","R3","R4","R5","R6")
    birkunda=baj_suv_data(Brigada,2,date,hudud_2,"R1","R2","R3","R4","R5","R6")
    h_2_R15=zip(h_2_R15,birkunda)
    
    #3
    hudud_3=hudud_list(Brigada,3)
    h_3_R15=baj_suv(Brigada,3,"R1","R2","R3","R4","R5","R6")
    birkunda=baj_suv_data(Brigada,3,date,hudud_3,"R1","R2","R3","R4","R5","R6")
    h_3_R15=zip(h_3_R15,birkunda)
   
   
    context={"user":user,"h_1_R15":h_1_R15,"h_2_R15":h_2_R15,"h_3_R15":h_3_R15,"date":date,"agranom1":agranom1,"agranom2":agranom2,"agranom3":agranom3}
    return render(request,'paxtasuv.html',context)

#GALLA SUVI
def g_suv(request):
    date=request.GET.get("date")
    user=request.user.profile
    date=datenow(date)
   
    #1
    hudud_1=hudud_list(Brigada,1)
    h_1_R15=baj_suv_g(Brigada,1,"G1","G2","G3","G4",'G5',"G6")
    birkunda=baj_suv_data_g(Brigada,1,date,hudud_1,"G1","G2","G3","G4",'G5',"G6")
    h_1_R15=zip(h_1_R15,birkunda)
    
    #2
    hudud_2=hudud_list(Brigada,2)
    h_2_R15=baj_suv_g(Brigada,2,"G1","G2","G3","G4",'G5',"G6")
    birkunda=baj_suv_data_g(Brigada,2,date,hudud_2,"G1","G2","G3","G4",'G5',"G6")
    h_2_R15=zip(h_2_R15,birkunda)
    
    #3
    hudud_3=hudud_list(Brigada,3)
    h_3_R15=baj_suv_g(Brigada,3,"G1","G2","G3","G4",'G5',"G6")
    birkunda=baj_suv_data_g(Brigada,3,date,hudud_3,"G1","G2","G3","G4",'G5',"G6")
    h_3_R15=zip(h_3_R15,birkunda)
   

    context={"user":user,"date":date,"h_1_R15":h_1_R15,"h_2_R15":h_2_R15,"h_3_R15":h_3_R15,"agranom1":agranom1,"agranom2":agranom2,"agranom3":agranom3}
    return render(request,'gallasuv.html',context)    


def chigit(request):
    date=request.GET.get("date")
    user=request.user.profile
    date=datenow(date)
   
    #1
    hudud_1=hudud_list(Brigada,1)
    h_1_R1=baj_ish_1(Brigada,1,"CH1")
    birkunda=baj_b_1(Brigada,1,date,hudud_1,"CH1")
    h_1_R1=zip(h_1_R1,birkunda)

    #2
    hudud_2=hudud_list(Brigada,2)
    h_2_R1=baj_ish_1(Brigada,2,"CH1")
    birkunda=baj_b_1(Brigada,2,date,hudud_2,"CH1")
    h_2_R1=zip(h_2_R1,birkunda)
    
    #3
    hudud_3=hudud_list(Brigada,3)
    h_3_R1=baj_ish_1(Brigada,3,"CH1")
    birkunda=baj_b_1(Brigada,3,date,hudud_3,"CH1")
    h_3_R1=zip(h_3_R1,birkunda)
    
    

    context={"user":user,"date":date,"agranom1":agranom1,"agranom2":agranom2,"agranom3":agranom3,"h_1_R1":h_1_R1,"h_2_R1":h_2_R1,"h_3_R1":h_3_R1}
    return render(request,'chigit.html',context)        


def oq_olish(request):
    
    date=request.GET.get("date")
    user=request.user.profile
    date=datenow(date)
    #1
    hudud_1=hudud_list(Brigada,1)
    h_1_R15=baj_ish(Brigada,1,"O1","O2")
    birkunda=baj_ish_data(Brigada,1,date,hudud_1,"O1","O2")
    h_1_R15=zip(h_1_R15,birkunda)
    #2
    hudud_2=hudud_list(Brigada,2)
    h_2_R15=baj_ish(Brigada,2,"O1","O2")
    birkunda=baj_ish_data(Brigada,2,date,hudud_2,"O1","O2")
    h_2_R15=zip(h_2_R15,birkunda)
    
    #3
    hudud_3=hudud_list(Brigada,3)
    h_3_R15=baj_ish(Brigada,3,"O1","O2")
    birkunda=baj_ish_data(Brigada,3,date,hudud_3,"O1","O2")
    h_3_R15=zip(h_3_R15,birkunda)
           
    context={"user":user,"h_1_R15":h_1_R15,"h_2_R15":h_2_R15,"h_3_R15":h_3_R15,"date":date,"agranom1":agranom1,"agranom2":agranom2,"agranom3":agranom3}
    
       
    return render(request,'oqariqolish.html',context)        

def oq_komish(request):
    
    date=request.GET.get("date")
    user=request.user.profile
    date=datenow(date)
    #1
    hudud_1=hudud_list(Brigada,1)
    h_1_R15=baj_ish(Brigada,1,"K1","K2")
    birkunda=baj_ish_data(Brigada,1,date,hudud_1,"K1","K2")
    h_1_R15=zip(h_1_R15,birkunda)
    #2
    hudud_2=hudud_list(Brigada,2)
    h_2_R15=baj_ish(Brigada,2,"K1","K2")
    birkunda=baj_ish_data(Brigada,2,date,hudud_2,"K1","K2")
    h_2_R15=zip(h_2_R15,birkunda)
    
    #3
    hudud_3=hudud_list(Brigada,3)
    h_3_R15=baj_ish(Brigada,3,"K1","K2")
    birkunda=baj_ish_data(Brigada,3,date,hudud_3,"K1","K2")
    h_3_R15=zip(h_3_R15,birkunda)
           
    context={"user":user,"h_1_R15":h_1_R15,"h_2_R15":h_2_R15,"h_3_R15":h_3_R15,"date":date,"agranom1":agranom1,"agranom2":agranom2,"agranom3":agranom3}
    
       
    return render(request,'oqariqkomish.html',context)           