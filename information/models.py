from django.db import models
from .choices import*

class NarxnomaS(models.Model):
    name=models.CharField(max_length=200)
    code=models.CharField(max_length=5)
    mex_tur=models.CharField(max_length=20,choices=mex_tur,null=True)
    brlik=models.CharField(max_length=20,choices=brlik)
    n_narx=models.FloatField(blank=True)
    k_narx=models.FloatField(blank=True)

    def save(self,*args,**kwargs):
        self.k_narx=round(self.n_narx*0.88,2)
        super().save(*args,**kwargs)
    def __str__(self):
        return str(self.name)

class BajarilganIshlar(models.Model):
    date=models.DateField(null=True)
    brigada=models.ForeignKey("Home.brigada",on_delete=models.CASCADE)
    ish_turi=models.ForeignKey("NarxnomaS",on_delete=models.CASCADE)
    miqdor=models.FloatField()
    n_summa=models.FloatField(blank=True,null=True)
    k_summa=models.FloatField(blank=True)


    def save(self,*args,**kwargs):
        self.k_summa=round(self.miqdor*self.ish_turi.n_narx,2)
        self.n_summa=round(self.miqdor*self.ish_turi.k_narx,2)
        super().save(*args,**kwargs)

    def __str__(self):
        return str(self.brigada)
