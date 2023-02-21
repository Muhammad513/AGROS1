from .models import*
from django.db.models import Sum

date1=Paxta.objects.filter(brigada__br_num=1).aggregate(Sum('sofVazn'))
