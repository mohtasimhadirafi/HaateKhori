let img = document.querySelector('#shape-back');
let btnCngLearnNext = document.querySelector('#learn-shape-next-btn');
let btnCngLearnBack = document.querySelector('#learn-shape-back-btn');
var shapeImageLearnCount =0;

btnCngLearnBack.style.visibility = 'hidden';

btnCngLearnNext.addEventListener('click' , ()=>{
    if ( shapeImageLearnCount == 0) {
        img.src = '/static/img/shape_triangle_learn.png';
        shapeImageLearnCount++;
        btnCngLearnBack.style.visibility = 'visible';
    }
    else if(shapeImageLearnCount == 1){
        img.src = '/static/img/shape_circle_learn.png';
        shapeImageLearnCount++;

    }
    else if(shapeImageLearnCount == 2){
        img.src = '/static/img/shape_quadrangle_learn.png';
        shapeImageLearnCount++;
    }
    else if(shapeImageLearnCount == 3){
        img.src = '/static/img/shape_together1_learn.png';

        btnCngLearnNext.style.visibility = 'hidden';
    }

})

btnCngLearnBack.addEventListener('click' , ()=>{
    if ( shapeImageLearnCount == 3) {
        img.src = '/static/img/shape_quadrangle_learn.png';
        shapeImageLearnCount--;

    }
    else if(shapeImageLearnCount == 2){
        img.src = '/static/img/shape_circle_learn.png';
        shapeImageLearnCount--;

    }
    else if(shapeImageLearnCount == 1){
        img.src = '/static/img/shape_triangle_learn.png';
        shapeImageLearnCount--;
    }
    else if(shapeImageLearnCount == 0){
        img.src = '/static/img/shape_line_img_background.png';
        btnCngLearnBack.style.visibility = 'hidden';
        btnCngLearnNext.style.visibility = 'visible';
    }
})