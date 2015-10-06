// script for drawing circuits

window.onload = function() {
    var paper = new Raphael(document.getElementById('canvas_container'), 1000, 1000);

    var resX = 400;
    var resY = 100;

    var resistor = paper.set (
        paper.circle(resX, resY, 5).attr({'fill': '#000000'}),
        paper.circle(resX + 145, resY, 5).attr({'fill': '#000000'}),
        paper.path("M " + resX + " " + resY + " l 25 0 l 10 20 l 18 -40 l 18 40 l 18 -40 l 18 40 l 10 -20 l 25 0")
        );

    resistor.attr({'stroke-width': 5, 'stroke-linejoin': 'round'});
    resistor.animate({transform: "r" + 90 + "," + resX + "," + resY}, 1000);
    // resistor.transform("r90,"+ "," + resX + "," + resY);

    var batX = 200;
    var batY = 100;

    var battery = paper.set (
        paper.circle(batX, batY, 5).attr({'fill': '#000000'}),
        paper.circle(batX, batY + 145, 5).attr({'fill': '#000000'}),
        paper.path("M " + batX + " " + batY + " l 0 50"), // top vertical
        paper.path("M " + (batX-50) + " " + (batY+50) + " l 100 0"), // top long bar
        paper.path("M " + (batX-20) + " " + (batY+65) + " l 40 0"), // middle short bar
        paper.path("M " + (batX-50) + " " + (batY+80) + " l 100 0"), // middle long bar
        paper.path("M " + (batX-20) + " " + (batY+95) + " l 40 0"), // bottom short bar
        paper.path("M " + batX + " " + (batY+95) + " l 0 50") // bottom vertical
    );

    battery.attr({'stroke-width': 5, 'stroke-linejoin': 'round'});
    //battery.animate({transform: "r" + -90 + "," + batX + "," + batY}, 1000);

    var segX = batX;
    var segY = batY;
    var segL = 50;

    while ((segX + segL) !== resX) {
        segL = segL*2;
    }

    var segment = paper.path("M " + segX + " " + segY + " l " + segL + " 0").attr({'stroke-width': 5, 'stroke-linejoin': 'round'});

    segY = segY + 145;

    var segment2 = paper.path("M " + segX + " " + segY + " l " + segL + " 0").attr({'stroke-width': 5, 'stroke-linejoin': 'round'});
}

// M -75 5 l 25 0