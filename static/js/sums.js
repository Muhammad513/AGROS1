var tds = document.getElementsByTagName('td');
console.log(tds)
var psum1 = 0;
var psum2 = 0;
var psum3 = 0;
var psum4 = 0;
var psum5 = 0;
var psum6 = 0;
var psum7 = 0;
var psum8 = 0;
var psum9 = 0;
var psum10 = 0;
var psum11 = 0;
var psum12 = 0;
var psum13 = 0;
var psum14 = 0;
var psum15 = 0;
var psum16 = 0;
var psum17 = 0;
var psum18 = 0;
var psum19 = 0;
var psum20 = 0;
var psum21 = 0;

for(var i = 0; i < tds.length; i ++) {
    if(tds[i].className == 'gek_1') {
        psum1 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'rej_1') {
        psum2 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'bir_1') {
        psum3 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'mav_1') {
        psum4 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'ski_1') {
        psum5 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'sen_1') {
        psum6 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'baj_1') {
        psum7 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    

}
for(var i = 0; i < tds.length; i ++) {
    if(tds[i].className == 'gektar2') {
        psum8 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'reja2') {
        psum9 += isNaN(tds[i].innerHTML) ? 0 :parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'birkunda2') {
        psum10 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'mavsumda2') {
        psum11 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'skidka2') {
        psum12 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'sent2') {
        psum13 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'bajarilish2') {
        psum14 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    

}
for(var i = 0; i < tds.length; i ++) {
    if(tds[i].className == 'gektar3') {
        psum15 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'reja3') {
        psum16 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'birkunda3') {
        psum17 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'mavsumda3') {
        psum18 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'skidka3') {
        psum19 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'sent3') {
        psum20 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'bajarilish3') {
        psum21 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    

}



document.getElementById('psumg1').innerHTML=psum1.toFixed(2)                                   
document.getElementById('psumg2').innerHTML=psum2.toFixed(2)                                              
document.getElementById('psumg3').innerHTML=psum3.toFixed(2)
document.getElementById('psumg4').innerHTML=psum4.toFixed(2)
document.getElementById('psumg5').innerHTML=psum5.toFixed(2)
document.getElementById('psumg6').innerHTML=((psum4/psum1)*10).toFixed(2)
document.getElementById('psumg7').innerHTML=(psum4*100/psum2).toFixed(2)
document.getElementById('psumg8').innerHTML=psum8.toFixed(2)
document.getElementById('psumg9').innerHTML=psum9.toFixed(2)
document.getElementById('psumg10').innerHTML=psum10.toFixed(2)
document.getElementById('psumg11').innerHTML=psum11.toFixed(2)
document.getElementById('psumg12').innerHTML=psum12.toFixed(2)
document.getElementById('psumg13').innerHTML=((psum11/psum8)*10).toFixed(2)
document.getElementById('psumg14').innerHTML=(psum11*100/psum9).toFixed(2)
document.getElementById('psumg15').innerHTML=psum15.toFixed(2)
document.getElementById('psumg16').innerHTML=psum16.toFixed(2)
document.getElementById('psumg17').innerHTML=psum17.toFixed(2)
document.getElementById('psumg18').innerHTML=psum18.toFixed(2)
document.getElementById('psumg19').innerHTML=psum19.toFixed(2)
document.getElementById('psumg20').innerHTML=((psum18/psum15)*10).toFixed(2)
document.getElementById('psumg21').innerHTML=(psum18*100/psum16).toFixed(2)
document.getElementById('psumg22').innerHTML=(psum1+psum8+psum15).toLocaleString()
document.getElementById('psumg23').innerHTML=(psum2+psum9+psum16).toLocaleString()
document.getElementById('psumg24').innerHTML=(psum3+psum10+psum17).toLocaleString()
document.getElementById('psumg25').innerHTML=(psum4+psum11+psum18).toLocaleString()
document.getElementById('psumg26').innerHTML=(psum5+psum12+psum19).toLocaleString()
document.getElementById('psumg27').innerHTML=((psum4+psum11+psum18)/(psum1+psum8+psum15)*10).toLocaleString()
document.getElementById('psumg28').innerHTML=((psum4+psum11+psum18)/(psum2+psum9+psum16)*100).toLocaleString()
