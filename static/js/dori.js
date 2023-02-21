var tds = document.getElementsByTagName('td');
var hsum1 = 0;
var hsum2 = 0;
var hsum3 = 0;
var hsum4 = 0;
var hsum5 = 0;
var hsum6 = 0;
var hsum7 = 0;
var hsum8 = 0;
var hsum9 = 0;
var hsum10 = 0;
var hsum11 = 0;
var hsum12 = 0;
var hsum13 = 0;



for(var i = 0; i < tds.length; i ++) {
    if(tds[i].className == 'gektar') {
        hsum1 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'birkunda1') {
        hsum2 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'amafos') {
        hsum3 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'miqdor1') {
        hsum4 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'qoldiq1') {
        hsum5 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'birkunda2') {
        hsum6 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'karbamit') {
        hsum7 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'miqdor2') {
        hsum8 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'qoldiq2') {
        hsum9 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'birkunda3') {
        hsum10 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'kali') {
        hsum11 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'miqdor3') {
        hsum12 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'qoldiq3') {
        hsum13 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
   


}


document.getElementById('dor_sum1').innerHTML=hsum1.toFixed(2)                                   
document.getElementById('dor_sum2').innerHTML=hsum2.toFixed(2)                                              
document.getElementById('dor_sum3').innerHTML=hsum3.toFixed(2)
document.getElementById('dor_sum4').innerHTML=hsum4.toFixed(2)
document.getElementById('dor_sum5').innerHTML=hsum5.toFixed(2)
document.getElementById('dor_sum6').innerHTML=hsum6.toFixed(2)
document.getElementById('dor_sum7').innerHTML=hsum7.toFixed(2)
document.getElementById('dor_sum8').innerHTML=hsum8.toFixed(2)
document.getElementById('dor_sum9').innerHTML=hsum9.toFixed(2)
document.getElementById('dor_sum10').innerHTML=hsum10.toFixed(2)
document.getElementById('dor_sum11').innerHTML=hsum11.toFixed(2)
document.getElementById('dor_sum12').innerHTML=hsum12.toFixed(2)
document.getElementById('dor_sum13').innerHTML=hsum13.toFixed(2)