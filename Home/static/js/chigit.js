var tds = document.getElementsByTagName('td');
var chsum1 = 0;
var chsum2 = 0;
var chsum3 = 0;
var chsum4 = 0;

var chsum5 = 0;
var chsum6 = 0;
var chsum7 = 0;
var chsum8 = 0;

var chsum9 = 0;
var chsum10 = 0;
var chsum11 = 0;
var chsum12 = 0;





for(var i = 0; i < tds.length; i ++) {
    if(tds[i].className == 'ch_gektar_1') {
        chsum1 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'ch_b_1') {
        chsum2 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'ch_m_1') {
        chsum3 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'ch_q_1') {
        chsum4 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
}

for(var i = 0; i < tds.length; i ++) {
    if(tds[i].className == 'ch_gektar_2') {
        chsum5 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'ch_b_2') {
        chsum6 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'ch_m_2') {
        chsum7 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'ch_q_2') {
        chsum8 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
}

for(var i = 0; i < tds.length; i ++) {
    if(tds[i].className == 'ch_gektar_3') {
        chsum9 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'ch_b_3') {
        chsum10 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'ch_m_3') {
        chsum11 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'ch_q_3') {
        chsum12 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
}



document.getElementById('chsum1').innerHTML=chsum1.toFixed(2)                                   
document.getElementById('chsum2').innerHTML=chsum2.toFixed(2)                                              
document.getElementById('chsum3').innerHTML=chsum3.toFixed(2)
document.getElementById('chsum4').innerHTML=chsum4.toFixed(2)

document.getElementById('chsum5').innerHTML=chsum5.toFixed(2)                                   
document.getElementById('chsum6').innerHTML=chsum6.toFixed(2)                                              
document.getElementById('chsum7').innerHTML=chsum7.toFixed(2)
document.getElementById('chsum8').innerHTML=chsum8.toFixed(2)

document.getElementById('chsum9').innerHTML=chsum9.toFixed(2)                                   
document.getElementById('chsum10').innerHTML=chsum10.toFixed(2)                                              
document.getElementById('chsum11').innerHTML=chsum11.toFixed(2)
document.getElementById('chsum12').innerHTML=chsum12.toFixed(2)



document.getElementById('chsum13').innerHTML=(chsum1+chsum5+chsum9).toFixed(1)                                   
document.getElementById('chsum14').innerHTML=(chsum2+chsum6+chsum10).toFixed(1)                                              
document.getElementById('chsum15').innerHTML=(chsum3+chsum7+chsum11).toFixed(1)
document.getElementById('chsum16').innerHTML=(chsum4+chsum8+chsum12).toFixed(1)

