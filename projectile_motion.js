//Variables
var initialVelocity = 10; // Initial velocity of the projectile
var initialAngle = 30; // Initial angle in grades
var gravity = 9.8; // Gravity acceleration
var time = 0; // time in seconds

//Calculates
var x = initialVelocity * Math.cos(initialAngle * Math.PI/180) * time; // position in X
var y = initialVelocity * Math.sin(initialAngle * Math.PI/180) * time - 0.5 * gravity * time * time; // position in Y

// Time increase
t += 0.1; // increasements of time in 0.1 seconds

// print position
console.log("Position in X: " + x + " Position in Y: " + y);
