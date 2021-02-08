let img = document.querySelector('#shape-back');
let btnCngLearnNext = document.querySelector('#learn-shape-next-btn');
let btnCngLearnBack = document.querySelector('#learn-shape-back-btn');
var shapeImageLearnCount =0;

btnCngLearnBack.style.visibility = 'hidden';

btnCngLearnNext.addEventListener('click' , ()=>{
    if ( shapeImageLearnCount == 0) {
        img.src = '/static/objectImage/book93dee123-cdd4-44be-835d-a295a320191a.jpg';
        shapeImageLearnCount++;
        btnCngLearnBack.style.visibility = 'visible';
    }
    else if(shapeImageLearnCount == 1){
        img.src = '/static/objectImage/bowl38743407-6621-41ed-8f64-6788a3cbf4da.jpg';
        shapeImageLearnCount++;

    }
    else if(shapeImageLearnCount == 2){
        img.src = '/static/objectImage/bowlf8278370-da48-4d99-8c55-1151f104b5ce.jpg';
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