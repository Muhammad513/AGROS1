from django.db.models import  F,IntegerField
import pickle
from django.shortcuts import render,redirect
from .models import*
from django.contrib.auth.decorators import login_required
from django.db.models import Sum,Count
from django.core import serializers
import json
from .full import*
from django.contrib.auth.models import User
from .forms import ChatMessageForm
import datetime
from Config.settings import agranom1,agranom2,agranom3
from information.function import hudud_list,baj_suv_data
import datetime
from information.models import BajarilganIshlar


@login_required(login_url='login')
def homePage(request):
    user=request.user.profile
    date=datetime.date.today()
 
    context={"user":user}
    return render(request,"office\office.html",context)



#--------------PAXTA-----------------------------------------------------------------

def PaxtaX(request):
    user=request.user.profile
    date=request.GET.get("date")
    date=datenow(date)
    #-1 Hudud
    hudud_1=hudud_list(Brigada,1)
    br_item_1=item_hudud(Brigada,1)
    birkunda=data_br(Brigada,1,date,hudud_1)
    print(birkunda,br_item_1)
    br_item_1=zip(br_item_1,birkunda)
    
    #-2 Hududu
    hudud_2=hudud_list(Brigada,2)
    br_item_2=item_hudud(Brigada,2)
    birkunda=data_br(Brigada,2,date,hudud_2)
    br_item_2=zip(br_item_2,birkunda)
    
    #-3 Hudud
    hudud_3=hudud_list(Brigada,3)
    br_item_3=item_hudud(Brigada,3)
    birkunda=data_br(Brigada,3,date,hudud_3)
    br_item_3=zip(br_item_3,birkunda)
     
    context={"br_item_1":br_item_1,"br_item_2":br_item_2,"br_item_3":br_item_3,"user":user,"date":date}
    return render(request,"Paxta\BaseP.html",context)


def hudud_p(request):
    user=request.user.profile
    date=request.GET.get("date")
    date=datenow(date)
    #1
    hudud1=hudud(Hudud,1)
    birkunda=hudud_b(Hudud,1,date)
    print(birkunda)
    hudud_1=zip(hudud1,birkunda)
    #2
    hudud2=hudud(Hudud,2)
    birkunda=hudud_b(Hudud,2,date)
    hudud_2=zip(hudud2,birkunda)
    #3
    hudud3=hudud(Hudud,3)
    birkunda=hudud_b(Hudud,3,date)
    print(hudud3,birkunda)
    hudud_3=zip(hudud3,birkunda)
    
    
    context={"hudud_1":hudud_1,"hudud_2":hudud_2,"hudud_3":hudud_3,"date":date}
    return render (request,'hudud/hudud.html',context)


def reestr_P(request):
    user=request.user.profile
    info=Paxta.objects.all().order_by('-date')
    context={'info':info,"user":user}
    return render(request,"Paxta/reestr.html",context)


def xarajat_p(request):
    
    user=request.user.profile
    context={'user':user}
    return render(request,"Paxta/xarajat.html",context)



#-------------GALLA-------------------------------------------------------------------------

def GallaX(request):
    
    user=request.user.profile
    date=request.GET.get("date")
    date=datenow(date)
        
    #-1 Hudud
    hudud_1=[1,2,3,4,5,6,7,8,9,10,33,34,35,40,41,42,43,44]
    br_item_1=item_hudud_G(Brigada,1)
    birkunda=data_br_G(Brigada,1,date,hudud_1)
    br_item_1=zip(br_item_1,birkunda)
    
    #-2 Hududu
    hudud_2=[11,12,13,14,15,16,17,18,19,20,21,35,36]
    br_item_2=item_hudud_G(Brigada,2)
    birkunda=data_br_G(Brigada,2,date,hudud_2)
    br_item_2=zip(br_item_2,birkunda)
    #-3 Hudud
    hudud_3=[22,23,24,25,26,27,28,29,30,31,32,37,38,39]
    br_item_3=item_hudud_G(Brigada,3)
    birkunda=data_br_G(Brigada,3,date,hudud_3)
    br_item_3=zip(br_item_3,birkunda)
     
    context={"br_item_1":br_item_1,"br_item_2":br_item_2,"br_item_3":br_item_3,"user":user,"date":date,"agranom1":agranom1,"agranom2":agranom2,"agranom3":agranom3}
    return render(request,"Galla\BaseG.html",context)


def reestrg(request):
    user=request.user.profile
    info=Galla.objects.all().order_by('-date')
    info=info.values("id",'date',"brigada__br_num",'yuk_num','brigada__br_full_name','tr_name','tr_marka','tr_num','sofVazn','ombor__name',"ombor__icon")
    context={'info':info,"user":user}
    return render(request,"Galla/reestr.html",context)




def omborG(request):
    date=request.GET.get("date")
    date=datenow(date)
    user=request.user.profile
    hudud_1=[1,2,3,4,5,6,7,8,9,10,33,34,35,40,41,42,43,44]
    br_item_1=item_ombor_G(OmborG,"DMK-1")
    br_item_2=item_ombor_G(OmborG,"DMK-2")
    br_item_3=item_ombor_G(OmborG,"ZAVOD")
    


    context={"user":user,'dmk1':br_item_1,'dmk2':br_item_2,'dmk3':br_item_3,"date":date}
    return render(request,"Galla/OmborG.html",context)


def xarajatG(request):
    user=request.user.profile
    

   
    context={"user":user,}
    return render(request,"Galla/xarajatG.html",context)


def hududg(request):
    user=request.user.profile
    date=request.GET.get("date")
    date=datenow(date)
    
    #1
    hudud1=hudud_g(Hudud,1)
    birkunda=hudud_g_b(Hudud,1,date)
    print(birkunda)
    hudud_1=zip(hudud1,birkunda)
    #2
    hudud2=hudud_g(Hudud,2)
    birkunda=hudud_g_b(Hudud,2,date)
    hudud_2=zip(hudud2,birkunda)
    #3
    hudud3=hudud_g(Hudud,3)
    birkunda=hudud_g_b(Hudud,3,date)
    hudud_3=zip(hudud3,birkunda)
   
    context={"hudud_1":hudud_1,"hudud_2":hudud_2,"hudud_3":hudud_3,"date":date,"user":user}
    return render(request,"hudud/hudud_g.html",context)



#-----------------------------------------------------------------------------------------------------














def naryad(request):
    br_num=request.GET.get('staff')
    ranges=request.GET.get('ranges')
    if ranges is None:
        ranges=ranges=list(range(1))
    else:
        ranges=list(range(int(ranges)))
    staff=Xodimlar.objects.filter(bolim__bolim=br_num)
    print(staff)
    context={"staff":staff,"ranges":ranges}
    return render(request,"ish haqqi/baseIsh.html",context)



def chat(request):
    user=Profile.objects.all()
    users=request.user.profile
    friends=users.friends.all()
    context={"user":user,"users":users,"friends":friends}
    return render(request,"chat/chat.html",context)    

def chatreq(request,pk):
    friend=Friend.objects.get(profile_id=pk)
    print(friend)
    users=request.user.profile
    profile=Profile.objects.get(id=friend.profile.id)
    chats=ChatMessage.objects.all()
    form=ChatMessageForm()
    
    user=Profile.objects.all()
    friends=users.friends.all()
    
    form=ChatMessageForm()
    if request.method=="POST":
        form=ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message=form.save(commit=False)
            chat_message.msg_sender=users
            chat_message.msg_receiver=profile
            chat_message.save()
            return redirect('chatreq',pk=friend.profile.id)

    context={"user":user,"users":users,"friend":friend,"friends":friends,"form":form,"profile":profile,'chats':chats}
    return render(request,"chat/srcchatbase.html",context)    


def testing(request):
    user=request.user.profile
    date=request.GET.get("date")
    date=datenow(date)

    fx_dori=dori(Kontragen,date,'AMAF1',"KAR1","KAL1")
    print(fx_dori)
    context={"fx_dori":fx_dori,"date":date}

    return render (request,'doriombor/dori.html',context)

