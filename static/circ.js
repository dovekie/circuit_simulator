// script for drawing circuits

window.onload = function() {
    var paper = new Raphael(document.getElementById('canvas_container'), 1000, 1000);

    var resX = 200;
    var resY = 100;

    var resistor = paper.set (
        paper.circle(resX, resY, 5).attr({'fill': '#000000'}),
        paper.circle(resX + 130, resY, 5).attr({'fill': '#000000'}),
        paper.path("M " + resX + " " + resY + " l 25 0 l 8 20 l 16 -40 l 16 40 l 16 -40 l 16 40 l 8 -20 l 25 0")
        );

    resistor.attr({'stroke-width': 5, 'stroke-linejoin': 'round'});

    resistor.animate({transform: "r" + 90 + "," + resX + "," + resY}, 1000);

}