var ballX;
var ballY;
var pressKey = false;
var m = 2;
function setup(){
	createCanvas(600,600);
	ballX = 20;
	ballY = 20;
}

function ballMoveRight(){
	ballX += m;
}
function ballMoveLeft(){
	ballX -= m;
}
function ballMoveUp(){
	ballY -= m;
}
function ballMoveDown(){
	ballY += m;
}

function draw(){
	background(0);
	fill(0,255,0);
	rect(0,0,40,40);
	fill(0,0,255);
	ellipse(ballX,ballY,30,30);
	fill(255,0,0);
	rect(275,560,40,40);
	noStroke();
	fill(255,255,0);
	rect(0,40,80,40);  // obst 1
	rect(120,0,40,120);  // obs 2
	rect(160,0,40,120);  // obs 3
	rect(240,0,360,40);  // obs 4
	rect(240,40,360,80);  // obs 5
	rect(0,120,40,40); // obs 6
	rect(80,160,220,40); // obs 7
	rect(0,240,120,80); // obs 8
	rect(120,240,200,40); // obs 9
	rect(120,280,120,40); // obs 10
	rect(0,320,80,160); // obs 11
	rect(0,480,160,120); // obs 12
	rect(160,480,120,80); // obs 13
	rect(360,160,160,40); // obs 14
	rect(360,200,80,280); // obs 15
	rect(280,320,80,40); // obs 16
	rect(440,200,40,120); // obs 17
	rect(120,360,240,80); // obs 18
	rect(360,480,40,40); // obs 19
	rect(320,480,40,80); // obs 20
	rect(560,120,40,120); // obs 21
	rect(520,240,80,360); // obs 22
	rect(480,400,40,200); // obs 23
	rect(440,520,40,80); // obs 24
	rect(400,560,40,40); // obs 25
	if (key==="d" && ballX<= 565) {
		ballMoveRight();
	}
	if (key==="a" && ballX >= 15) {
		ballMoveLeft();
	}
	if (key==="s" && ballY <= 580) {
		ballMoveDown();
	}
	if (key==="w" && ballY >= 15) {
		ballMoveUp();
	}
	if (key===" ") {
		ballX = 20;
		ballY = 20;
	}

	// setting the bounderies for the walls so when the edge of the circle touches the wall it will be brought back to it's original pission on the green sqaure.
	if (ballX <= 80 && ballY == 30) {
		ballX = 20;
		ballY = 20;
	}
	// if (ballX == 80 && ballY >= 30 && ballY <= 80) {
	// 	ballX = 20;
	// 	ballY = 20;
	// }
}
