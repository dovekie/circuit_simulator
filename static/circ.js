// script for drawing circuits

// circuit elements are 140 long and 50 wide (resistors are 40 wide + margins; battery is 25 wide + margins)
// elements should be separated by at least 100 (for 50 clearance from edge to edge)

Raphael.fn.resistorGroup = function(batX, batY, numResistors, relationship) { 
    /* Build a set of resistors
       Takes the battery's X and Y coords, the number of resistors in the group,
       And a string that is either "series" or "parallel"
       Returns a Raphael set.
    */
    this.relationship = relationship;
    this.numResistors = numResistors;
    this.resX = batX + 100;
    if (this.relationship === "series") {
        this.resY = batY - 70;
    } else {
        this.resY = batY;
    }

    var Group = this.set();

    for (var i = 0; i < numResistors; i++) {
        var newResistor = this.set(
            this.circle(this.resX, this.resY, 5)
                .attr({'fill': '#000000'}),
            this.circle(this.resX + 140, this.resY, 5)
                .attr({'fill': '#000000'}),
            this.path("M " + this.resX + " " + this.resY + " l 24 0 l 9 20 l 18 -40 l 17 40 l 18 -40 l 18 40 l 9 -20 l 24 0")
                .attr({'stroke-width': 5, 'stroke-linejoin': 'round'})
            );

        if (this.relationship === "series") {
            newResistor.transform("r90," + this.resX + "," + this.resY);
        }

        Group.push(newResistor);

        this.resY = this.resY + 140;
    } 
    return Group;
}

window.onload = function () {
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

    var res1 = paper.resistorGroup(batX, batY, 2, "series");

    var res2 = paper.resistorGroup(batX+100, batY+70, 1, "series");
}

// how to animate! for reference.
    // battery.animate({transform: "r" + -90 + "," + batX + "," + batY}, 1000);