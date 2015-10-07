// script for drawing circuits

// circuit elements are 140 long and 50 wide (resistors are 40 wide + margins; battery has no margins)
// elements should be separated by at least 100 (for 50 clearance from edge to edge)

var numResistors = 4;

window.onload = function() {
    var paper = new Raphael(document.getElementById('canvas_container'), 1000, 1000);
    var batX = 100;
    var batY = 100;

    var battery = paper.set (
        paper.circle(batX, batY, 3).attr({'fill': '#000000'}),
        paper.circle(batX, batY + 140, 3).attr({'fill': '#000000'}),
        paper.path("M " + batX + " " + batY + " l 0 45"), // top vertical
        paper.path("M " + (batX-25) + " " + (batY+45) + " l 50 0"), // top long bar
        paper.path("M " + (batX-10) + " " + (batY+60) + " l 20 0"), // middle short bar
        paper.path("M " + (batX-25) + " " + (batY+75) + " l 50 0"), // middle long bar
        paper.path("M " + (batX-10) + " " + (batY+90) + " l 20 0"), // bottom short bar
        paper.path("M " + batX + " " + (batY+90) + " l 0 45") // bottom vertical
    );

    battery.attr({'stroke-width': 5, 'stroke-linejoin': 'round'});

    var relationship = "parallel";
    var parallelGroup = paper.set();
    var resX = batX + 100;
    if (relationship === "parallel") {
        var resY = batY - 70;
    } else {
        var resY = batY;
    }

    for (var i = 0; i < numResistors; i++) {
        var newResistor = paper.set(
            paper.circle(resX, resY, 5)
                .attr({'fill': '#000000'}),
            paper.circle(resX + 140, resY, 5)
                .attr({'fill': '#000000'}),
            paper.path("M " + resX + " " + resY + " l 24 0 l 9 20 l 18 -40 l 17 40 l 18 -40 l 18 40 l 9 -20 l 24 0")
                .attr({'stroke-width': 5, 'stroke-linejoin': 'round'})
            );

        if (relationship === "series") {
            newResistor.transform("r90," + resX + "," + resY);
        }

        parallelGroup.push (
            newResistor
        );

        resY = resY + 140;
    } 

    // var resX = 100;
    // var resY = 100;

    // var parallelGroup = paper.set()

    // for (var i = 0; i < numResistors; i++) {
    //      resY = resY + (i * 100);
    //      parallelGroup.push (
    //         paper.circle(resX, resY, 5)
    //             .attr({'fill': '#000000'}),
    //         paper.circle(resX + 140, resY, 5)
    //             .attr({'fill': '#000000'}),
    //         paper.path("M " + resX + " " + resY + " l 24 0 l 9 20 l 18 -40 l 17 40 l 18 -40 l 18 40 l 9 -20 l 24 0")
    //             .attr({'stroke-width': 5, 'stroke-linejoin': 'round'})//,
    //         paper.path("M " + (resX + (i * 140)) + " " + (resY - (i * 100)) + " l 0 100")
    //             .attr({'stroke-width': 5, 'stroke-linejoin': 'round'})
    //         );
    // } // this ends your for loop

    // parallelGroup.transform("r90,"+ (100 + (145/2)) + "," + (100 + (resY/4)) + ",t23,-250");



    // var wire1 = paper.path("M" + batX + " " + batY + "L370 100").attr({'stroke-width': 5, 'stroke-linejoin': 'round'});

    // var wire2 = paper.path("M" + batX + " " + (batY + 145) + "L370 245").attr({'stroke-width': 5, 'stroke-linejoin': 'round'});

}

// how to animate! for reference.
    // battery.animate({transform: "r" + -90 + "," + batX + "," + batY}, 1000);