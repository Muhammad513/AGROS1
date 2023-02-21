var tds = document.getElementsByTagName('td');
var asum1 = 0;
var asum2 = 0;
var asum3 = 0;
var asum4 = 0;

var asum5 = 0;
var asum6 = 0;
var asum7 = 0;
var asum8 = 0;

var asum9 = 0;
var asum10 = 0;
var asum11 = 0;
var asum12 = 0;





for(var i = 0; i < tds.length; i ++) {
    if(tds[i].className == 'k_b_a_1') {
        asum1 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'k_m_a_1') {
        asum2 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 't_b_a_1') {
        asum3 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 't_m_a_1') {
        asum4 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
}


for(var i = 0; i < tds.length; i ++) {
    if(tds[i].className == 'k_b_a_2') {
        asum5 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'k_m_a_2') {
        asum6 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 't_b_a_2') {
        asum7 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 't_m_a_2') {
        asum8 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
}


for(var i = 0; i < tds.length; i ++) {
    if(tds[i].className == 'k_b_a_3') {
        asum9 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 'k_m_a_3') {
        asum10 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 't_b_a_3') {
        asum11 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
    else if(tds[i].className == 't_m_a_3') {
        asum12 += isNaN(tds[i].innerHTML) ? 0 : parseFloat(tds[i].innerHTML);
    }
}


document.getElementById('jsum1').innerHTML=asum1.toFixed(2)                                   
document.getElementById('jsum2').innerHTML=asum2.toFixed(2)                                              
document.getElementById('jsum3').innerHTML=asum3.toFixed(2)
document.getElementById('jsum4').innerHTML=asum4.toFixed(2)

document.getElementById('jsum5').innerHTML=asum5.toFixed(2)                                   
document.getElementById('jsum6').innerHTML=asum6.toFixed(2)                                              
document.getElementById('jsum7').innerHTML=asum7.toFixed(2)
document.getElementById('jsum8').innerHTML=asum8.toFixed(2)

document.getElementById('jsum9').innerHTML=asum9.toFixed(2)                                   
document.getElementById('jsum10').innerHTML=asum10.toFixed(2)                                              
document.getElementById('jsum11').innerHTML=asum11.toFixed(2)
document.getElementById('jsum12').innerHTML=asum12.toFixed(2)

document.getElementById('jsum13').innerHTML=(asum1+asum5+asum9).toFixed(1)                                   
document.getElementById('jsum14').innerHTML=(asum2+asum6+asum10).toFixed(1)                                              
document.getElementById('jsum15').innerHTML=(asum3+asum7+asum11).toFixed(1)
document.getElementById('jsum16').innerHTML=(asum4+asum8+asum12).toFixed(1)