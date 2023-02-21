var tds = document.getElementsByTagName('td');
var hsum1 = 0;
var hsum2 = 0;
var hsum3 = 0;
var hsum4 = 0;
var hsum5 = 0;
var hsum6 = 0;
var hsum7 = 0;


for(var i = 0; i < tds.length; i ++) {
    if(tds[i].className == 'gektar_agro') {
        hsum1 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'reja_agro') {
        hsum2 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'birkunda_agro') {
        hsum3 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'mavsumda_agro') {
        hsum4 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'skidka_agro') {
        hsum5 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'sentner_agro') {
        hsum6 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'bajarilish_agro') {
        hsum7 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }

}


document.getElementById('agro_sum1').innerHTML=hsum1.toFixed(2)                                   
document.getElementById('agro_sum2').innerHTML=hsum2.toFixed(2)                                              
document.getElementById('agro_sum3').innerHTML=hsum3.toFixed(2)
document.getElementById('agro_sum4').innerHTML=hsum4.toFixed(2)
document.getElementById('agro_sum5').innerHTML=hsum5.toFixed(2)
document.getElementById('agro_sum6').innerHTML=((hsum4/hsum1)*10).toFixed(2)
document.getElementById('agro_sum7').innerHTML=(hsum4*100/hsum2).toFixed(2)