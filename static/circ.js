// script for drawing circuits

var numResistors = 2;

window.onload = function() {
    var paper = new Raphael(document.getElementById('canvas_container'), 1000, 1000);

    var resX = 100;
    var resY = 100;

    var parallelGroup = paper.set()

    for (var i = 0; i < numResistors; i++) {
         resY = resY + (i * 100);
         parallelGroup.push (
            paper.circle(resX, resY, 5)
                .attr({'fill': '#000000'}),
            paper.circle(resX + 145, resY, 5)
                .attr({'fill': '#000000'}),
            paper.path("M " + resX + " " + resY + " l 25 0 l 10 20 l 18 -40 l 18 40 l 18 -40 l 18 40 l 10 -20 l 25 0")
                .attr({'stroke-width': 5, 'stroke-linejoin': 'round'}),
            paper.path("M " + (resX + (i * 145)) + " " + (resY - (i * 100)) + " l 0 100")
                .attr({'stroke-width': 5, 'stroke-linejoin': 'round'})
            );

    } // this ends your for loop

    parallelGroup.transform("r90,"+ (100 + (145/2)) + "," + (100 + (resY/4)) + ",t23,-250");

    // paper.circle((100 + (145/2)), (100 + (resY/4)), 10);

    // resX = 400;
    // var resistor = paper.set (
    //     paper.circle(resX, resY, 5).attr({'fill': '#000000'}),
    //     paper.circle(resX + 145, resY, 5).attr({'fill': '#000000'}),
    //     paper.path("M " + resX + " " + resY + " l 25 0 l 10 20 l 18 -40 l 18 40 l 18 -40 l 18 40 l 10 -20 l 25 0")
    //     );

    // resistor.attr({'stroke-width': 5, 'stroke-linejoin': 'round'});
    // resistor.animate({transform: "r" + 90 + "," + resX + "," + resY}, 1000);
    // resistor.transform("r90,"+ "," + resX + "," + resY);

    var batX = 200;
    var batY = 100;

    var battery = paper.set (
        paper.circle(batX, batY, 3).attr({'fill': '#000000'}),
        paper.circle(batX, batY + 145, 3).attr({'fill': '#000000'}),
        paper.path("M " + batX + " " + batY + " l 0 50"), // top vertical
        paper.path("M " + (batX-50) + " " + (batY+50) + " l 100 0"), // top long bar
        paper.path("M " + (batX-20) + " " + (batY+65) + " l 40 0"), // middle short bar
        paper.path("M " + (batX-50) + " " + (batY+80) + " l 100 0"), // middle long bar
        paper.path("M " + (batX-20) + " " + (batY+95) + " l 40 0"), // bottom short bar
        paper.path("M " + batX + " " + (batY+95) + " l 0 50") // bottom vertical
    );

    battery.attr({'stroke-width': 5, 'stroke-linejoin': 'round'});
    //battery.animate({transform: "r" + -90 + "," + batX + "," + batY}, 1000);

    var wire1 = paper.path("M" + batX + " " + batY + "L370 100").attr({'stroke-width': 5, 'stroke-linejoin': 'round'});

    var wire2 = paper.path("M" + batX + " " + (batY + 145) + "L370 245").attr({'stroke-width': 5, 'stroke-linejoin': 'round'});

    // var segX = batX;
    // var segY = batY;
    // var segL = 50;

    // while ((segX + segL) !== resX) {
    //     segL = segL + 10;
    // }

    // var segment = paper.path("M " + segX + " " + segY + " l " + segL + " 0").attr({'stroke-width': 5, 'stroke-linejoin': 'round'});

    // segY = segY + 145;

    // var segment2 = paper.path("M " + segX + " " + segY + " l " + segL + " 0").attr({'stroke-width': 5, 'stroke-linejoin': 'round'});
}