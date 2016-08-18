var runnerX;
var runnerY;
var steps;
var speed = 0;
var runnerName;
var cImg;
var runImg;
var runner;
var startButton;
var lives = [0,0,0];
var hPage = true;
var title;

// the environment
var ground, sun, cloud, skyBack;
var tree, bush, flowers;
var treeX, bushX, flowersX;
var fr = 49;
var treeImg, bushImg, flowersImg;
var soundTrkOne;
var jumping = 1000;
var gravity = 1;
var onfloor;
var gameOn;
var time, score;
var sC, c, s;
var stepCounter;
function setup() {
	var myCan = createCanvas(windowWidth, windowHeight);
  	myCan.parent('p5Container');
	cImg = createImg("http://vignette1.wikia.nocookie.net/sonic/images/3/34/Sonic_-_Sonic_Colors_Artwork_-_(1).png/revision/latest?cb=20101111191347");
	cImg.position(windowWidth/3, windowHeight/6);
	skyBack = loadImage("img/skybackground.jpg");
	ground = loadImage("img/ground.png");
	sun = loadImage("img/sun.png");
	gameOn = false;
	jumping = false;
	//soundTrkOne = loadSound('img/cityEscape.mp3');
	title = createP("RUNNERS GO!!!");
	title.position(windowWidth/4, windowHeight/17 - 500);
	title.style("font-size", "300pt");
	//textSize(400);
	//textAlign(CENTER);
	//text("Runners Go!!!", windowWidth/2, windowHeight/6.4);
	startButton = createButton("RUN NOW");
	startButton.position(windowWidth/2, windowHeight/2);
	startButton.size(300,200);
	startButton.mousePressed(runGame);
  	treeX = width;
  	bushX = width/.5;
  	flowersX = width/.8;
  	frameRate(fr);
  	runnerX = skyBack.width/.5;
  	runnerY = skyBack.height/.45;
  	onfloor = skyBack.height/.45;
  	sC = 5;
  	t = 0;
  	c = 0;
  	s = 0;
  	stepCounter = createP("");
  	time = createP(" ");
  	score = createP(" ");
  	if (keyCode == ENTER) {
		runGame();
	}

 }


function draw(){
	if(gameOn == false) {
		background(240,240,0);
	}
	//background(0,91,241);
	if (hPage == false){
		//if(sC > 0) {
		s += 1;
		c += 1;
		if (c % 45 == 0) {
			sC -= 1;
			t += 1;
		}

		if (sC == 0) {
			noLoop();
			textSize(100);
			textAlign(CENTER);
			score.remove();
			text("NO MORE STEPS!. NOW GO OUT AND DO MORE ACTIVITIES TO GAIN MORE PLAY TIME!", skyBack.width/.45, skyBack.height/1.7);
		}
		//}
		
		stepCounter.remove();
		stepCounter = createP("STEP COUNT: " + sC);
		stepCounter.position(skyBack.width/.3, skyBack.height/2.5 - 200);
		stepCounter.style("font-size", "84pt");
		time.remove();
		time = createP("TIME: " + t + "s");
		time.position(skyBack.width/2.3, skyBack.height/2.5 - 200);
		time.style("font-size", "84pt");
		score.remove();
		score = createP("SCORE: " + s + "pts");
		score.position(skyBack.width/.5, skyBack.height/2.3);
		score.style("font-size", "84pt");
			//sC.Delay(500);

		gameOn = true;
		// creating bushes for mvement.
		bushX = bushX -= 200;
		bushImg.remove();
		bushImg = createImg("img/bush.png");
		bushImg.position(bushX, skyBack.height/.41);
		bushImg.size(2000,500);
		if (bushX <= 0) {
			if(fr == 49) {
				fr = 50;
				frameRate(fr);
				
			} else {
				frameRate(fr);
				bushX = width/.5;
				bushX = bushX -= 200;
			}
		}
		// making the flowers in the background "move"
		flowersX = flowersX -= 700;
		flowersImg.remove();
		flowersImg = createImg("img/flowers.png");
		flowersImg.position(flowersX, skyBack.height/.39);
		flowersImg.size(2000,200);
		if (flowersX <= 0) {
			if(fr == 49) {
				fr = 50;
				frameRate(fr);
				
			} else {
				frameRate(fr);
				flowersX = width/.8;
				flowersX = flowersX -= 700;
			}
		}

		//making the trees in background "move"
		treeX = treeX -= 500;
		treeImg.remove();
		treeImg = createImg("img/tree.png");
		treeImg.position(treeX, skyBack.height/2.68);
		treeImg.size(2000,1800);
		if (treeX <= 0) {
			if(fr == 49) {
				fr = 50;
				frameRate(fr);
				
			} else {
				frameRate(fr);
				treeX = width;
				treeX = treeX -= 500;
			}
		}

		//runner.velocity.y += gravity;

		// making the character jump
		// if (runner.collide(ground)) {
		// 	runner.velocity.y = 0;	
		// }
		if (keyDown("j")) {
			console.log("jump");

			//runner.velocity.y -jumping;
			//jumping = createImg("img/sonicJump.gif");
			//jumping.position(skyBack.width/.5, skyBack.height/.45);
		}
		//create home page in p5
		//if click on p5 start game button
			//then hPage = false
	}

}

function runGame(){
	hPage = false;
	startButton.remove();
	cImg.remove();
	title.remove();
	background(255);
	//background.remove();
	// soundTrkOne.setVolume(1);
	// soundTrkOne.play();
	//soundTrkOne.loop();


	// setting the enviornment
	image(skyBack,0,0, displayWidth, displayHeight);
	image(ground, 0, height/1.3, windowWidth, skyBack.height/1.01);
	image(sun, skyBack.width/.5, skyBack.height/9, skyBack.width/3, skyBack.height/2);

	//creating image for the tree
	treeImg = createImg("img/tree.png");
	treeImg.position(treeX, skyBack.height/1.3);

	// creating image for the bush
	bushImg = createImg("img/bush.png");
	bushImg.position(bushX, height/2.4);

	// creating image for the flowers
	flowersImg = createImg("img/flowers.png");
	flowersImg.position(flowersX, skyBack.height/1.3);

	// creating image for the runner\ph
	runner = createImg("img/sonicrunning.gif");
	runner.position(skyBack.width/.5, skyBack.height/.45);
	runner.size(900,500);
	//runnerJump();
}

// function runnerJump() {
// 	console.log("hi");
// 	runnerY = runnerY -= 750;
// 	runner.remove();
// 	jumping = createImg("img/sonicJump.gif");
// 	jumping.position(runnerX, runnerY);
// 	jumping.size(800,800);
// 	jumping.remove();
// 	jumping = createImg("img/sonicJump.gif");
// 	jumping.position(runnerX, runnerY);
// 	jumping.size(800,800);
// 	while(runnerY > onfloor) {
// 		if(fr == 49) {
// 			fr = 50;
// 			frameRate(fr);	
// 		} else {
// 			frameRate(fr);
// 			runnerY = runnerY += 350;
// 		}
// 	}
// 	if (runnerY <= onfloor) {
// 		runner = createImg("img/sonicrunning.gif");
// 		runner.position(skyBack.width/.5, skyBack.height/.45);
// 		runner.size(900,500);
// 	} else {
// 		runnerY = onfloor;
// 	}
// }

   