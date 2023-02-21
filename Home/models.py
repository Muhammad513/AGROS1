from django.db import models
from django.contrib.auth.models import User
from .choices import brlik,tr_marka,mx_turi


# Create your models here.
class Paxta(models.Model):
    date=models.DateField(null=True)
    sofVazn=models.IntegerField()
    ifloslik=models.FloatField()
    namlik=models.FloatField()
    punkt=models.ForeignKey('Punkt',on_delete=models.CASCADE,null=True)
    brigada=models.ForeignKey('Brigada',on_delete=models.CASCADE,null=True)
    xisobi=models.FloatField(blank=True)
    kond=models.FloatField(blank=True)
   
    def save(self,*args,**kwargs):
        self.xisobi=round((self.sofVazn*((100-self.ifloslik)/98)),1)
        self.kond=round((self.sofVazn*((100-self.ifloslik)/98))*(109/(100+self.namlik)),1)
        super().save(*args,**kwargs)

    def __str__(self):
         return str(self.sofVazn)    

#------------------GALLA--------------------------------------------
class Galla(models.Model):
    date=models.DateField(null=True)
    brigada=models.ForeignKey('Brigada',on_delete=models.CASCADE,null=True)
    sofVazn=models.IntegerField(blank=True)
    ombor=models.ForeignKey("OmborG",on_delete=models.CASCADE,blank=True)
    yuk_num=models.CharField(max_length=3,blank=True)
    tr_marka=models.CharField(max_length=20,choices=tr_marka,blank=True)
    tr_num=models.CharField(max_length=20,blank=True)
    tr_name=models.CharField(max_length=30,null=True,blank=True)
    imzo=models.BooleanField(default=False)

    def __str__(self):
        return str(self.sofVazn)

class OmborG(models.Model):
    name=models.CharField(max_length=30)
    icon=models.ImageField(upload_to='icon',blank=True,null=True,default='img/DEFAULT.ico')
    reja=models.FloatField(null=True)
    sentner=models.FloatField(null=True)

    def __str__(self):
        return str(self.name)





#-------------------------------------------------------------------









class Brigada(models.Model):
    br_num=models.IntegerField()
    br_full_name=models.CharField(max_length=200)
    massiv=models.ForeignKey('Massiv',on_delete=models.CASCADE)
    hudud=models.ForeignKey("Hudud",on_delete=models.CASCADE,null=True)
    G_gektar=models.FloatField()
    P_gektar=models.FloatField()
    G_reja=models.FloatField()
    P_reja=models.FloatField()
    
    def __str__(self):
        return str(self.br_num)

class Punkt(models.Model):
    name=models.CharField(max_length=200)        
    def __str__(self):
        return str(self.name)

class Massiv(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Hudud(models.Model):
    h_num=models.IntegerField()
    Agranom_full_name=models.CharField(max_length=200)
    def __str__(self):
        return str(self.Agranom_full_name)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name= models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    pic=models.ImageField(upload_to='img',blank=True,null=True,default='img/default.jpg')
    friends=models.ManyToManyField('Friend',related_name='my_friend',blank=True)
    lavozim=models.OneToOneField('Lavozim',on_delete=models.CASCADE,blank=True,null=True)


    def __str__(self):
        return self.first_name

class Lavozim(models.Model):
    name=models.CharField(max_length=30)
    bolim=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.name


class Friend(models.Model):
    profile=models.OneToOneField('Profile',on_delete=models.CASCADE,null=True)



    def __str__(self):
        return self.profile.first_name

class ChatMessage(models.Model):
    body=models.CharField(max_length=1000)
    msg_sender=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="msg_sender")
    msg_receiver=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="msg_receiver")
    seen=models.BooleanField(default=False)


    def __str__(self):
        return self.body
        
#---------------------------------------------------------------------------------
class Maxsulot(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)



class Narxnoma(models.Model):
    ish_turi=models.CharField(max_length=200)
    narxi=models.FloatField()
    brlik=models.CharField(max_length=20)

    def __str__(self):
        return str(self.ish_turi)



class Ishxaqqi(models.Model):
    date=models.DateField(null=True)
    xodimlar=models.ForeignKey('Xodimlar',on_delete=models.CASCADE,null=True)
    xarajat_turi=models.ForeignKey('Maxsulot',on_delete=models.CASCADE)
    ish_turi=models.ForeignKey('Narxnoma',on_delete=models.CASCADE)
    brigada=models.ForeignKey("Brigada",on_delete=models.CASCADE)
    kolvo=models.FloatField()
    summa=models.FloatField(blank=True)

    def save(self,*args,**kwargs):
        self.summa=round(self.ish_turi.narxi*self.kolvo,1)
        super().save(*args,**kwargs)

    def __str__(self):
        return str(self.xodimlar)


class Xodimlar(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    bolim=models.ForeignKey('Lavozim',on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return str(f'{self.first_name } {self.last_name}')
    


class DoriOmbor(models.Model):
    dori_name=models.CharField(max_length=200)
    narxi=models.FloatField()
    code=models.CharField(max_length=5)

    def __str__(self):
         return str(self.dori_name)



class Kontragen(models.Model):
    fx_name=models.CharField(max_length=200)
    massiv=models.CharField(max_length=15,null=True)
    amaf_reja=models.FloatField(null=True)
    karb_reja=models.FloatField(null=True)
    kali_reja=models.FloatField(null=True)
    maydon=models.FloatField()
    sent=models.FloatField()
    xosil=models.FloatField()


    def __str__(self):
         return str(self.fx_name)


class DoriSend(models.Model):
    date=models.DateField(null=True)
    fermer=models.ForeignKey('Kontragen',on_delete=models.CASCADE)
    dori_tur=models.ForeignKey('DoriOmbor',on_delete=models.CASCADE)
    kolvo=models.FloatField()
    summa=models.FloatField(blank=True)

    
    def save(self,*args,**kwargs):
        self.summa=round((self.kolvo*self.dori_tur.narxi),1)
        super().save(*args,**kwargs)

    def __str__(self):
         return str(self.fermer)    

