function goToEnglishNumber(){
    window.location.href = "/english_number";
}

function goToBanglaCharecter() {
    window.location.href = "/bangla_charecter";
}

function goToBanglaNumber() {
    window.location.href = "/bangla_number";
}

function goToEnglishCharecter() {
    window.location.href = "/writing"
}

var container = document.getElementById('contain-slider');
let btnSlider = document.querySelector('#slidebar-option');



btnSlider.addEventListener('click' , ()=> {
    container.style.visibility = 'visible';
})
