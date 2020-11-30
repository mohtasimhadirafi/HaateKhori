var canvas, ctx,
    brush = {
        x: 0,
        y: 0,
        color: '#ffffff',
        size: 20,
        down: false,
    },
    strokes = [],
    currentStroke = null;

function redraw() {
    ctx.clearRect(0, 0, canvas.width(), canvas.height());
    ctx.lineCap = 'round';
    for (var i = 0; i < strokes.length; i++) {
        var s = strokes[i];
        ctx.strokeStyle = s.color;
        ctx.lineWidth = s.size;
        ctx.beginPath();
        ctx.moveTo(s.points[0].x, s.points[0].y);
        for (var j = 0; j < s.points.length; j++) {
            var p = s.points[j];
            ctx.lineTo(p.x, p.y);
        }
        ctx.stroke();
    }
}


function erase() {
    console.log("Hit");
    console.log(brush.x);

}

function init() {
    canvas = $('#draw');
    canvas.attr({
        width: window.innerWidth,
        height: window.innerHeight,
    });
    ctx = canvas[0].getContext('2d');
    canvas[0].width = 1000;
    canvas[0].height = 530;

    function mouseEvent(e) {
        brush.x = e.pageX-430;
        brush.y = e.pageY-190;

        console.log("Mousedown event");

        currentStroke.points.push({
            x: brush.x,
            y: brush.y,
        });

        redraw();
    }

    function downloadImage(data, filename = 'untitled.png') {
        var a = document.createElement('a');
        a.href = data;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
    }

    canvas.mousedown(function (e) {
        brush.down = true;

        currentStroke = {
            color: "#ffffff",
            size: brush.size,
            points: [],
        };

        strokes.push(currentStroke);

        mouseEvent(e);
    }).mouseup(function (e) {
        brush.down = false;

        mouseEvent(e);

        currentStroke = null;
    }).mousemove(function (e) {
        if (brush.down)
            mouseEvent(e);
    });

    $('#save-btn').click(function () {
        var image = canvas[0].toDataURL("image/png").replace("image/png", "image/octet-stream");
        downloadImage(image, 'my-canvas.png')
    });

    $('#undo-btn').click(function () {
        strokes.pop();
        redraw();
    });

    $('#clear-btn').click(function () {
        strokes = [];
        redraw();
    });

    $('#erase-btn').click(function () {
        erase();
    });

    $('#color-picker').on('input', function () {
        brush.color = this.value;
    });

    $('#brush-size').on('input', function () {
        brush.size = this.value;
    });
}

$(init);