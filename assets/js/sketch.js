//<script src="assets\js\p5.js"></script>

//GLOBAL VARIABLES
const particles = [];
//create an object to hold the Kinect data
function setup() {
      // check if the device is running on mobile
  //isMobile = (navigator.userAgent.indexOf("Mobile") !== -1);

  //if (isMobile) {
    //var canvas = createCanvas(windowWidth, windowHeight);

    var canvas = createCanvas(window.innerWidth, window.innerHeight);

    const particlesLength = Math.floor(window.innerWidth*3); //number of Particles is 3 times width of the window
  
    for (let i = 0; i < particlesLength; i++) {
      particles.push(new Particle()); //initialize a new Particle for every spot in the particles array
    }
    if (canvas) {
      canvas.parent('container1');
  } else {
      console.log("The element with ID 'container1' does not exist in the HTML.");
  }
    

    
  }
  //}
  
  function draw() {
    background(0);
  
    let mousePos = createVector(mouseX, mouseY); //replace with Kinect data
  
    particles.forEach(function(p, index) {
      p.update();
      p.draw();
      p.attracted(mousePos);
  
    });
  
    // If you press any key on the keyboard, a circle will appear
    // and follow the position of your mouse around.
    // fill(255);
    // if (keyIsPressed == true) {
    // circle(mouseX, mouseY, 80);
    // }
  
  }


  class Particle {

    constructor() {
      this.pos = createVector(random(width), random(height));
      this.size = random(1, 2);
      this.color = random(100, 255); //define how see thru each particle is
      this.vel = createVector(random(-1, 1), random(-1, 1))
      this.acc = createVector(random(-0.1, 0.1), random(-0.1, 0.1)); //set the acceleration of each particle
      this.mass = this.size; //set the mass of each particle to be the same as its size 
      // this.prevSize = [];
      // this.history = [];
  
    }
  
    //Draw a single Particle
    draw() {
      noStroke();
      fill(this.color);
      circle(this.pos.x, this.pos.y, this.size);
  
      //Draw a trail behind each particle//
      // for (let i = 0; i = this.history.length; i++) {
      //   let prevPos = this.history[i];
      //   fill(255, 255, 255, this.alpha);
      //   circle(prevPos.x, prevPos.y, this.size);
      // }
    }
  
    //Particle rises or falls and bounces off the edges
    update() {
      this.pos.add(this.vel); //add velocity to the x, y positions to make it move
      this.vel.add(this.acc); //add acceleration to the velocity to mimic physics
      this.detectEdges();
      // this.attracted();
  
      // Push the position of the circle to history array
      // this.history.push(this.pos);
  
      // Make the particles repel away from the cursor
    }
  
    detectEdges() {
  
      // If the Particle touches the left or right edges of the canvas,
      // it will reverse direction.
      if(this.pos.x < 0 || this.pos.x > width) {
        this.vel.x *= -1;
      }
  
      // If the Particle touches the top or bottom edges of the canvas,
      // it will reverse direction.
      if(this.pos.y < 0 || this.pos.y > height) {
        this.vel.y *= -1;
      }
    }
  
    attracted(mousePos) {
      let force = p5.Vector.sub(mousePos, this.pos); //the force on each particle moves in is the target position minus its current position (also its distance)
      let distSquared = force.magSq(); //the distance between current and target position squared (will be used to calculate gravity force enacted on particle)
      let grav = -1000; //set the gravity enacted on the particle (based on universal gravitational constant)
      let magnitude = grav / distSquared; //the magnitude of the force enacted on each particle
      force.setMag(magnitude);
      this.acc = force;
    }
  
  }