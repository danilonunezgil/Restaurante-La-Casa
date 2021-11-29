var btnaddcart = document.getElementById('btn-open-popup');
var overlay = document.getElementById('overlay');
var popup = document.getElementById('popup');
var btnclose = document.getElementById('btn-close');

btnaddcart.addEventListener('click', function(){
    overlay.classList.add('active');
    popup.classList.add('active')
});

btnclose.addEventListener('click', function(){
    overlay.classList.remove('active');
    popup.classList.remove('active');
});